"""OnlinePush Packet Builder.

This module is used to build and handle OnlinePush packets.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""

from typing import Optional

from jce import JceField, JceStruct, types


class DelMsgInfo(JceStruct):
    """OnlinePush Delete Message Info Packet.

    Note:
        Source: OnlinePushPack.DelMsgInfo
    """

    from_uin: types.INT64 = JceField(jce_id=0)
    msg_time: types.INT64 = JceField(jce_id=1)
    msg_seq: types.INT8 = JceField(jce_id=2)
    msg_cookies: types.BYTES = JceField(bytes(), jce_id=3)
    cmd: types.INT8 = JceField(0, jce_id=4)
    msg_type: types.INT64 = JceField(0, jce_id=5)
    app_id: types.INT64 = JceField(0, jce_id=6)
    send_time: types.INT64 = JceField(0, jce_id=7)
    sso_seq: types.INT32 = JceField(0, jce_id=8)
    sso_ip: types.INT32 = JceField(0, jce_id=9)
    client_ip: types.INT32 = JceField(0, jce_id=10)


class DeviceInfo(JceStruct):
    """OnlinePush Device Info Packet.

    Note:
        Source: OnlinePushPack.DeviceInfo
    """

    net_type: types.BYTE = JceField(bytes(1), jce_id=0)
    dev_type: types.STRING = JceField("", jce_id=1)
    os_ver: types.STRING = JceField("", jce_id=2)
    vendor_name: types.STRING = JceField("", jce_id=3)
    vendor_os_name: types.STRING = JceField("", jce_id=4)
    ios_idfa: types.STRING = JceField("", jce_id=5)


class MsgInfo(JceStruct):
    from_uin: types.INT64 = JceField(jce_id=0)
    msg_time: types.INT64 = JceField(jce_id=1)
    msg_type: types.INT8 = JceField(jce_id=2)
    msg_seq: types.INT8 = JceField(jce_id=3)
    str_msg: types.STRING = JceField("", jce_id=4)
    real_msg_time: types.INT32 = JceField(0, jce_id=5)
    msg: types.BYTES = JceField(jce_id=6)
    share_id: types.INT64 = JceField(0, jce_id=7)
    msg_cookie: types.BYTES = JceField(bytes(), jce_id=8)
    app_share_cookie: types.BYTES = JceField(bytes(), jce_id=9)
    msg_uid: types.INT64 = JceField(0, jce_id=10)
    last_change_time: types.INT64 = JceField(0, jce_id=11)
    # TODO: missed


class SvcRespPushMsg(JceStruct):
    """OnlinePush Service Push Response Packet.

    Note:
        Source: OnlinePushPack.SvcRespPushMsg
    """

    uin: types.INT64 = JceField(jce_id=0)
    del_infos: types.LIST[DelMsgInfo] = JceField(jce_id=1)
    svrip: types.INT32 = JceField(jce_id=2)
    push_token: Optional[types.BYTES] = JceField(None, jce_id=3)
    service_type: types.INT32 = JceField(0, jce_id=4)
    device_info: Optional[DeviceInfo] = JceField(None, jce_id=5)


class _SvcReqPushMsg(JceStruct):
    uin: types.INT64 = JceField(jce_id=0)
    msg_time: types.INT64 = JceField(jce_id=1)
    msg_info: types.LIST[MsgInfo] = JceField(jce_id=2)
    svrip: types.INT32 = JceField(0, jce_id=3)
    sync_cookie: types.BYTES = JceField(bytes(), jce_id=4)


class SvcReqPushMsg(JceStruct):
    body: _SvcReqPushMsg = JceField(jce_id=0)
