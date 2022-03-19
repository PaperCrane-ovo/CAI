"""Example Code for Login.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import os
import asyncio
import signal
import asyncio
import sys
import traceback
from io import BytesIO

from PIL import Image

from cai.api import Client, make_client
from cai.exceptions import (
    LoginException,
    ApiResponseError,
    LoginDeviceLocked,
    LoginSliderNeeded,
    LoginAccountFrozen,
    LoginCaptchaNeeded,
)


async def run(closed: asyncio.Event):
    account = os.getenv("ACCOUNT", "")
    password = os.getenv("PASSWORD")
    try:
        assert password and account, ValueError("account or password not set")

        account = int(account)
        ci = Client(make_client(account, password))

        try:
            await ci.login()
            print(f"Login Success! Client status: {ci.client.status!r}")
        except Exception as e:
            await handle_failure(ci, e)
    finally:
        closed.set()


async def handle_failure(client: Client, exception: Exception):
    if isinstance(exception, LoginSliderNeeded):
        print("Verify url:", exception.verify_url)
        ticket = input("Please enter the ticket: ").strip()
        try:
            await client.submit_slider_ticket(ticket)
            print("Login Success!")
            await asyncio.sleep(3)
        except Exception as e:
            await handle_failure(client, e)
    elif isinstance(exception, LoginCaptchaNeeded):
        print("Captcha:")
        image = Image.open(BytesIO(exception.captcha_image))
        image.show()
        captcha = input("Please enter the captcha: ").strip()
        try:
            await client.submit_captcha(captcha, exception.captcha_sign)
            print("Login Success!")
            await asyncio.sleep(3)
        except Exception as e:
            await handle_failure(client, e)
    elif isinstance(exception, LoginAccountFrozen):
        print("Account is frozen!")
    elif isinstance(exception, LoginDeviceLocked):
        print("Device lock detected!")
        way = (
            "sms"
            if exception.sms_phone
            else "url"
            if exception.verify_url
            else ""
        )
        if exception.sms_phone and exception.verify_url:
            while True:
                choice = input(
                    f"1. Send sms message to {exception.sms_phone}.\n"
                    f"2. Verify device by scanning.\nChoose: "
                )
                if "1" in choice:
                    way = "sms"
                    break
                elif "2" in choice:
                    way = "url"
                    break
                print(f"'{choice}' is not valid!")
        if not way:
            print("No way to verify device...")
        elif way == "sms":
            await client.request_sms()
            print(f"SMS was sent to {exception.sms_phone}!")
            sms_code = input("Please enter the sms_code: ").strip()
            try:
                await client.submit_sms(sms_code)
            except Exception as e:
                await handle_failure(client, e)
        elif way == "url":
            await client.close()
            print(f"Go to {exception.verify_url} to verify device!")
            input("Press ENTER after verification to continue login...")
            try:
                await client.login()
            except Exception as e:
                await handle_failure(client, e)
    elif isinstance(exception, LoginException):
        print("Login Error:", repr(exception))
    elif isinstance(exception, ApiResponseError):
        print("Response Error:", repr(exception))
    else:
        print("Unknown Error:", repr(exception))
        traceback.print_exc()


if __name__ == "__main__":
    close = asyncio.Event()

    async def wait_cleanup():
        await close.wait()

    loop = asyncio.get_event_loop()
    loop.create_task(run(close))
    try:
        loop.run_until_complete(wait_cleanup())
    except KeyboardInterrupt:
        close.set()
