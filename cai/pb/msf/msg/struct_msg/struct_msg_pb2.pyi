"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from builtins import (
    bool,
    bytes,
    int,
)

from google.protobuf.descriptor import (
    Descriptor,
    FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message,
)

from typing import (
    Iterable,
    Optional,
    Text,
)

from typing_extensions import (
    Literal,
)


DESCRIPTOR: FileDescriptor

class AddFrdSNInfo(Message):
    DESCRIPTOR: Descriptor
    NOTSEEDYNAMIC_FIELD_NUMBER: int
    SETSN_FIELD_NUMBER: int
    notSeeDynamic: int
    setSn: int
    def __init__(self,
        *,
        notSeeDynamic: Optional[int] = ...,
        setSn: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["notSeeDynamic",b"notSeeDynamic","setSn",b"setSn"]) -> bool: ...
    def ClearField(self, field_name: Literal["notSeeDynamic",b"notSeeDynamic","setSn",b"setSn"]) -> None: ...

class FlagInfo(Message):
    DESCRIPTOR: Descriptor
    GRPMSG_KICK_ADMIN_FIELD_NUMBER: int
    GRPMSG_HIDDENGRP_FIELD_NUMBER: int
    GRPMSG_WORDINGDOWN_FIELD_NUMBER: int
    FRDMSG_GETBUSICARD_FIELD_NUMBER: int
    GRPMSG_GETOFFICIALACCOUNT_FIELD_NUMBER: int
    GRPMSG_GETPAYINGROUP_FIELD_NUMBER: int
    FRDMSG_DISCUSS2MANYCHAT_FIELD_NUMBER: int
    GRPMSG_NOTALLOWJOINGRP_INVITENOTFRD_FIELD_NUMBER: int
    FRDMSG_NEEDWAITINGMSG_FIELD_NUMBER: int
    FRDMSGUINT32NEEDALLUNREADMSG_FIELD_NUMBER: int
    GRPMSG_NEEDAUTOADMINWORDING_FIELD_NUMBER: int
    GRPMSGGETTRANSFERGROUPMSGFLAG_FIELD_NUMBER: int
    GRPMSGGETQUITPAYGROUPMSGFLAG_FIELD_NUMBER: int
    GRPMSGSUPPORTINVITEAUTOJOIN_FIELD_NUMBER: int
    GRPMSGMASKINVITEAUTOJOIN_FIELD_NUMBER: int
    GRPMSG_GETDISBANDEDBYADMIN_FIELD_NUMBER: int
    GRPMSG_GETC2CINVITEJOINGROUP_FIELD_NUMBER: int
    GrpMsg_Kick_Admin: int
    GrpMsg_HiddenGrp: int
    GrpMsg_WordingDown: int
    FrdMsg_GetBusiCard: int
    GrpMsg_GetOfficialAccount: int
    GrpMsg_GetPayInGroup: int
    FrdMsg_Discuss2ManyChat: int
    GrpMsg_NotAllowJoinGrp_InviteNotFrd: int
    FrdMsg_NeedWaitingMsg: int
    FrdMsgUint32NeedAllUnreadMsg: int
    GrpMsg_NeedAutoAdminWording: int
    GrpMsgGetTransferGroupMsgFlag: int
    GrpMsgGetQuitPayGroupMsgFlag: int
    GrpMsgSupportInviteAutoJoin: int
    GrpMsgMaskInviteAutoJoin: int
    GrpMsg_GetDisbandedByAdmin: int
    GrpMsg_GetC2CInviteJoinGroup: int
    def __init__(self,
        *,
        GrpMsg_Kick_Admin: Optional[int] = ...,
        GrpMsg_HiddenGrp: Optional[int] = ...,
        GrpMsg_WordingDown: Optional[int] = ...,
        FrdMsg_GetBusiCard: Optional[int] = ...,
        GrpMsg_GetOfficialAccount: Optional[int] = ...,
        GrpMsg_GetPayInGroup: Optional[int] = ...,
        FrdMsg_Discuss2ManyChat: Optional[int] = ...,
        GrpMsg_NotAllowJoinGrp_InviteNotFrd: Optional[int] = ...,
        FrdMsg_NeedWaitingMsg: Optional[int] = ...,
        FrdMsgUint32NeedAllUnreadMsg: Optional[int] = ...,
        GrpMsg_NeedAutoAdminWording: Optional[int] = ...,
        GrpMsgGetTransferGroupMsgFlag: Optional[int] = ...,
        GrpMsgGetQuitPayGroupMsgFlag: Optional[int] = ...,
        GrpMsgSupportInviteAutoJoin: Optional[int] = ...,
        GrpMsgMaskInviteAutoJoin: Optional[int] = ...,
        GrpMsg_GetDisbandedByAdmin: Optional[int] = ...,
        GrpMsg_GetC2CInviteJoinGroup: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["FrdMsgUint32NeedAllUnreadMsg",b"FrdMsgUint32NeedAllUnreadMsg","FrdMsg_Discuss2ManyChat",b"FrdMsg_Discuss2ManyChat","FrdMsg_GetBusiCard",b"FrdMsg_GetBusiCard","FrdMsg_NeedWaitingMsg",b"FrdMsg_NeedWaitingMsg","GrpMsgGetQuitPayGroupMsgFlag",b"GrpMsgGetQuitPayGroupMsgFlag","GrpMsgGetTransferGroupMsgFlag",b"GrpMsgGetTransferGroupMsgFlag","GrpMsgMaskInviteAutoJoin",b"GrpMsgMaskInviteAutoJoin","GrpMsgSupportInviteAutoJoin",b"GrpMsgSupportInviteAutoJoin","GrpMsg_GetC2CInviteJoinGroup",b"GrpMsg_GetC2CInviteJoinGroup","GrpMsg_GetDisbandedByAdmin",b"GrpMsg_GetDisbandedByAdmin","GrpMsg_GetOfficialAccount",b"GrpMsg_GetOfficialAccount","GrpMsg_GetPayInGroup",b"GrpMsg_GetPayInGroup","GrpMsg_HiddenGrp",b"GrpMsg_HiddenGrp","GrpMsg_Kick_Admin",b"GrpMsg_Kick_Admin","GrpMsg_NeedAutoAdminWording",b"GrpMsg_NeedAutoAdminWording","GrpMsg_NotAllowJoinGrp_InviteNotFrd",b"GrpMsg_NotAllowJoinGrp_InviteNotFrd","GrpMsg_WordingDown",b"GrpMsg_WordingDown"]) -> bool: ...
    def ClearField(self, field_name: Literal["FrdMsgUint32NeedAllUnreadMsg",b"FrdMsgUint32NeedAllUnreadMsg","FrdMsg_Discuss2ManyChat",b"FrdMsg_Discuss2ManyChat","FrdMsg_GetBusiCard",b"FrdMsg_GetBusiCard","FrdMsg_NeedWaitingMsg",b"FrdMsg_NeedWaitingMsg","GrpMsgGetQuitPayGroupMsgFlag",b"GrpMsgGetQuitPayGroupMsgFlag","GrpMsgGetTransferGroupMsgFlag",b"GrpMsgGetTransferGroupMsgFlag","GrpMsgMaskInviteAutoJoin",b"GrpMsgMaskInviteAutoJoin","GrpMsgSupportInviteAutoJoin",b"GrpMsgSupportInviteAutoJoin","GrpMsg_GetC2CInviteJoinGroup",b"GrpMsg_GetC2CInviteJoinGroup","GrpMsg_GetDisbandedByAdmin",b"GrpMsg_GetDisbandedByAdmin","GrpMsg_GetOfficialAccount",b"GrpMsg_GetOfficialAccount","GrpMsg_GetPayInGroup",b"GrpMsg_GetPayInGroup","GrpMsg_HiddenGrp",b"GrpMsg_HiddenGrp","GrpMsg_Kick_Admin",b"GrpMsg_Kick_Admin","GrpMsg_NeedAutoAdminWording",b"GrpMsg_NeedAutoAdminWording","GrpMsg_NotAllowJoinGrp_InviteNotFrd",b"GrpMsg_NotAllowJoinGrp_InviteNotFrd","GrpMsg_WordingDown",b"GrpMsg_WordingDown"]) -> None: ...

class FriendInfo(Message):
    DESCRIPTOR: Descriptor
    JOINTFRIEND_FIELD_NUMBER: int
    BLACKLIST_FIELD_NUMBER: int
    jointFriend: Text
    blacklist: Text
    def __init__(self,
        *,
        jointFriend: Optional[Text] = ...,
        blacklist: Optional[Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["blacklist",b"blacklist","jointFriend",b"jointFriend"]) -> bool: ...
    def ClearField(self, field_name: Literal["blacklist",b"blacklist","jointFriend",b"jointFriend"]) -> None: ...

class GroupInfo(Message):
    DESCRIPTOR: Descriptor
    GROUPAUTHTYPE_FIELD_NUMBER: int
    DISPLAYACTION_FIELD_NUMBER: int
    ALERT_FIELD_NUMBER: int
    DETAILALERT_FIELD_NUMBER: int
    OTHERADMINDONE_FIELD_NUMBER: int
    APPPRIVILEGEFLAG_FIELD_NUMBER: int
    groupAuthType: int
    displayAction: int
    alert: Text
    detailAlert: Text
    otherAdminDone: Text
    appPrivilegeFlag: int
    def __init__(self,
        *,
        groupAuthType: Optional[int] = ...,
        displayAction: Optional[int] = ...,
        alert: Optional[Text] = ...,
        detailAlert: Optional[Text] = ...,
        otherAdminDone: Optional[Text] = ...,
        appPrivilegeFlag: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["alert",b"alert","appPrivilegeFlag",b"appPrivilegeFlag","detailAlert",b"detailAlert","displayAction",b"displayAction","groupAuthType",b"groupAuthType","otherAdminDone",b"otherAdminDone"]) -> bool: ...
    def ClearField(self, field_name: Literal["alert",b"alert","appPrivilegeFlag",b"appPrivilegeFlag","detailAlert",b"detailAlert","displayAction",b"displayAction","groupAuthType",b"groupAuthType","otherAdminDone",b"otherAdminDone"]) -> None: ...

class MsgInviteExt(Message):
    DESCRIPTOR: Descriptor
    SRCTYPE_FIELD_NUMBER: int
    SRCCODE_FIELD_NUMBER: int
    WAITSTATE_FIELD_NUMBER: int
    srcType: int
    srcCode: int
    waitState: int
    def __init__(self,
        *,
        srcType: Optional[int] = ...,
        srcCode: Optional[int] = ...,
        waitState: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["srcCode",b"srcCode","srcType",b"srcType","waitState",b"waitState"]) -> bool: ...
    def ClearField(self, field_name: Literal["srcCode",b"srcCode","srcType",b"srcType","waitState",b"waitState"]) -> None: ...

class MsgPayGroupExt(Message):
    DESCRIPTOR: Descriptor
    JOINGRPTIME_FIELD_NUMBER: int
    QUITGRPTIME_FIELD_NUMBER: int
    joinGrpTime: int
    quitGrpTime: int
    def __init__(self,
        *,
        joinGrpTime: Optional[int] = ...,
        quitGrpTime: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["joinGrpTime",b"joinGrpTime","quitGrpTime",b"quitGrpTime"]) -> bool: ...
    def ClearField(self, field_name: Literal["joinGrpTime",b"joinGrpTime","quitGrpTime",b"quitGrpTime"]) -> None: ...

class ReqNextSystemMsg(Message):
    DESCRIPTOR: Descriptor
    NUM_FIELD_NUMBER: int
    FOLLOWINGFRIENDSEQ_FIELD_NUMBER: int
    FOLLOWINGGROUPSEQ_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    FLAG_FIELD_NUMBER: int
    LANGUAGE_FIELD_NUMBER: int
    VERSION_FIELD_NUMBER: int
    FRIENDMSGTYPEFLAG_FIELD_NUMBER: int
    REQMSGTYPE_FIELD_NUMBER: int
    num: int
    followingFriendSeq: int
    followingGroupSeq: int
    checktype: int
    @property
    def flag(self) -> FlagInfo: ...
    language: int
    version: int
    friendMsgTypeFlag: int
    reqMsgType: int
    def __init__(self,
        *,
        num: Optional[int] = ...,
        followingFriendSeq: Optional[int] = ...,
        followingGroupSeq: Optional[int] = ...,
        checktype: Optional[int] = ...,
        flag: Optional[FlagInfo] = ...,
        language: Optional[int] = ...,
        version: Optional[int] = ...,
        friendMsgTypeFlag: Optional[int] = ...,
        reqMsgType: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","flag",b"flag","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","friendMsgTypeFlag",b"friendMsgTypeFlag","language",b"language","num",b"num","reqMsgType",b"reqMsgType","version",b"version"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","flag",b"flag","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","friendMsgTypeFlag",b"friendMsgTypeFlag","language",b"language","num",b"num","reqMsgType",b"reqMsgType","version",b"version"]) -> None: ...

class ReqSystemMsg(Message):
    DESCRIPTOR: Descriptor
    NUM_FIELD_NUMBER: int
    LATESTFRIENDSEQ_FIELD_NUMBER: int
    LATESTGROUPSEQ_FIELD_NUMBER: int
    VERSION_FIELD_NUMBER: int
    LANGUAGE_FIELD_NUMBER: int
    num: int
    latestFriendSeq: int
    latestGroupSeq: int
    version: int
    language: int
    def __init__(self,
        *,
        num: Optional[int] = ...,
        latestFriendSeq: Optional[int] = ...,
        latestGroupSeq: Optional[int] = ...,
        version: Optional[int] = ...,
        language: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["language",b"language","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","num",b"num","version",b"version"]) -> bool: ...
    def ClearField(self, field_name: Literal["language",b"language","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","num",b"num","version",b"version"]) -> None: ...

class ReqSystemMsgAction(Message):
    DESCRIPTOR: Descriptor
    TYPE_FIELD_NUMBER: int
    SEQ_FIELD_NUMBER: int
    REQUIN_FIELD_NUMBER: int
    SUBTYPE_FIELD_NUMBER: int
    SRCID_FIELD_NUMBER: int
    SUBSRCID_FIELD_NUMBER: int
    GROUPMSGTYPE_FIELD_NUMBER: int
    ACTIONINFO_FIELD_NUMBER: int
    LANGUAGE_FIELD_NUMBER: int
    type: int
    seq: int
    reqUin: int
    subType: int
    srcId: int
    subSrcId: int
    groupMsgType: int
    @property
    def actionInfo(self) -> SystemMsgActionInfo: ...
    language: int
    def __init__(self,
        *,
        type: Optional[int] = ...,
        seq: Optional[int] = ...,
        reqUin: Optional[int] = ...,
        subType: Optional[int] = ...,
        srcId: Optional[int] = ...,
        subSrcId: Optional[int] = ...,
        groupMsgType: Optional[int] = ...,
        actionInfo: Optional[SystemMsgActionInfo] = ...,
        language: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["actionInfo",b"actionInfo","groupMsgType",b"groupMsgType","language",b"language","reqUin",b"reqUin","seq",b"seq","srcId",b"srcId","subSrcId",b"subSrcId","subType",b"subType","type",b"type"]) -> bool: ...
    def ClearField(self, field_name: Literal["actionInfo",b"actionInfo","groupMsgType",b"groupMsgType","language",b"language","reqUin",b"reqUin","seq",b"seq","srcId",b"srcId","subSrcId",b"subSrcId","subType",b"subType","type",b"type"]) -> None: ...

class ReqSystemMsgNew(Message):
    DESCRIPTOR: Descriptor
    NUM_FIELD_NUMBER: int
    LATESTFRIENDSEQ_FIELD_NUMBER: int
    LATESTGROUPSEQ_FIELD_NUMBER: int
    VERSION_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    FLAG_FIELD_NUMBER: int
    LANGUAGE_FIELD_NUMBER: int
    ISGETFRDRIBBON_FIELD_NUMBER: int
    ISGETGRPRIBBON_FIELD_NUMBER: int
    FRIENDMSGTYPEFLAG_FIELD_NUMBER: int
    REQMSGTYPE_FIELD_NUMBER: int
    num: int
    latestFriendSeq: int
    latestGroupSeq: int
    version: int
    checktype: int
    @property
    def flag(self) -> FlagInfo: ...
    language: int
    isGetFrdRibbon: bool
    isGetGrpRibbon: bool
    friendMsgTypeFlag: int
    reqMsgType: int
    def __init__(self,
        *,
        num: Optional[int] = ...,
        latestFriendSeq: Optional[int] = ...,
        latestGroupSeq: Optional[int] = ...,
        version: Optional[int] = ...,
        checktype: Optional[int] = ...,
        flag: Optional[FlagInfo] = ...,
        language: Optional[int] = ...,
        isGetFrdRibbon: Optional[bool] = ...,
        isGetGrpRibbon: Optional[bool] = ...,
        friendMsgTypeFlag: Optional[int] = ...,
        reqMsgType: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","flag",b"flag","friendMsgTypeFlag",b"friendMsgTypeFlag","isGetFrdRibbon",b"isGetFrdRibbon","isGetGrpRibbon",b"isGetGrpRibbon","language",b"language","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","num",b"num","reqMsgType",b"reqMsgType","version",b"version"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","flag",b"flag","friendMsgTypeFlag",b"friendMsgTypeFlag","isGetFrdRibbon",b"isGetFrdRibbon","isGetGrpRibbon",b"isGetGrpRibbon","language",b"language","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","num",b"num","reqMsgType",b"reqMsgType","version",b"version"]) -> None: ...

class ReqSystemMsgRead(Message):
    DESCRIPTOR: Descriptor
    LATESTFRIENDSEQ_FIELD_NUMBER: int
    LATESTGROUPSEQ_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    REQMSGTYPE_FIELD_NUMBER: int
    latestFriendSeq: int
    latestGroupSeq: int
    type: int
    checktype: int
    reqMsgType: int
    def __init__(self,
        *,
        latestFriendSeq: Optional[int] = ...,
        latestGroupSeq: Optional[int] = ...,
        type: Optional[int] = ...,
        checktype: Optional[int] = ...,
        reqMsgType: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","reqMsgType",b"reqMsgType","type",b"type"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","reqMsgType",b"reqMsgType","type",b"type"]) -> None: ...

class RspHead(Message):
    DESCRIPTOR: Descriptor
    RESULT_FIELD_NUMBER: int
    FAIL_FIELD_NUMBER: int
    result: int
    fail: Text
    def __init__(self,
        *,
        result: Optional[int] = ...,
        fail: Optional[Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["fail",b"fail","result",b"result"]) -> bool: ...
    def ClearField(self, field_name: Literal["fail",b"fail","result",b"result"]) -> None: ...

class RspNextSystemMsg(Message):
    DESCRIPTOR: Descriptor
    HEAD_FIELD_NUMBER: int
    MSGS_FIELD_NUMBER: int
    FOLLOWINGFRIENDSEQ_FIELD_NUMBER: int
    FOLLOWINGGROUPSEQ_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    GAMENICK_FIELD_NUMBER: int
    UNDECIDFORQIM_FIELD_NUMBER: int
    UNREADCOUNT3_FIELD_NUMBER: int
    @property
    def head(self) -> RspHead: ...
    @property
    def msgs(self) -> RepeatedCompositeFieldContainer[StructMsg]: ...
    followingFriendSeq: int
    followingGroupSeq: int
    checktype: int
    gameNick: Text
    undecidForQim: bytes
    unReadCount3: int
    def __init__(self,
        *,
        head: Optional[RspHead] = ...,
        msgs: Optional[Iterable[StructMsg]] = ...,
        followingFriendSeq: Optional[int] = ...,
        followingGroupSeq: Optional[int] = ...,
        checktype: Optional[int] = ...,
        gameNick: Optional[Text] = ...,
        undecidForQim: Optional[bytes] = ...,
        unReadCount3: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","gameNick",b"gameNick","head",b"head","unReadCount3",b"unReadCount3","undecidForQim",b"undecidForQim"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","gameNick",b"gameNick","head",b"head","msgs",b"msgs","unReadCount3",b"unReadCount3","undecidForQim",b"undecidForQim"]) -> None: ...

class RspSystemMsg(Message):
    DESCRIPTOR: Descriptor
    HEAD_FIELD_NUMBER: int
    MSGS_FIELD_NUMBER: int
    UNREADCOUNT_FIELD_NUMBER: int
    LATESTFRIENDSEQ_FIELD_NUMBER: int
    LATESTGROUPSEQ_FIELD_NUMBER: int
    FOLLOWINGFRIENDSEQ_FIELD_NUMBER: int
    FOLLOWINGGROUPSEQ_FIELD_NUMBER: int
    DISPLAY_FIELD_NUMBER: int
    @property
    def head(self) -> RspHead: ...
    @property
    def msgs(self) -> RepeatedCompositeFieldContainer[StructMsg]: ...
    unreadCount: int
    latestFriendSeq: int
    latestGroupSeq: int
    followingFriendSeq: int
    followingGroupSeq: int
    display: Text
    def __init__(self,
        *,
        head: Optional[RspHead] = ...,
        msgs: Optional[Iterable[StructMsg]] = ...,
        unreadCount: Optional[int] = ...,
        latestFriendSeq: Optional[int] = ...,
        latestGroupSeq: Optional[int] = ...,
        followingFriendSeq: Optional[int] = ...,
        followingGroupSeq: Optional[int] = ...,
        display: Optional[Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["display",b"display","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","head",b"head","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","unreadCount",b"unreadCount"]) -> bool: ...
    def ClearField(self, field_name: Literal["display",b"display","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","head",b"head","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","msgs",b"msgs","unreadCount",b"unreadCount"]) -> None: ...

class RspSystemMsgAction(Message):
    DESCRIPTOR: Descriptor
    HEAD_FIELD_NUMBER: int
    DETAIL_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    INVALIDDECIDED_FIELD_NUMBER: int
    REMARKRESULT_FIELD_NUMBER: int
    @property
    def head(self) -> RspHead: ...
    detail: Text
    type: int
    invalidDecided: Text
    remarkResult: int
    def __init__(self,
        *,
        head: Optional[RspHead] = ...,
        detail: Optional[Text] = ...,
        type: Optional[int] = ...,
        invalidDecided: Optional[Text] = ...,
        remarkResult: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["detail",b"detail","head",b"head","invalidDecided",b"invalidDecided","remarkResult",b"remarkResult","type",b"type"]) -> bool: ...
    def ClearField(self, field_name: Literal["detail",b"detail","head",b"head","invalidDecided",b"invalidDecided","remarkResult",b"remarkResult","type",b"type"]) -> None: ...

class RspSystemMsgNew(Message):
    DESCRIPTOR: Descriptor
    HEAD_FIELD_NUMBER: int
    UNREADFRIENDCOUNT_FIELD_NUMBER: int
    UNREADGROUPCOUNT_FIELD_NUMBER: int
    LATESTFRIENDSEQ_FIELD_NUMBER: int
    LATESTGROUPSEQ_FIELD_NUMBER: int
    FOLLOWINGFRIENDSEQ_FIELD_NUMBER: int
    FOLLOWINGGROUPSEQ_FIELD_NUMBER: int
    FRIENDMSGS_FIELD_NUMBER: int
    GROUPMSGS_FIELD_NUMBER: int
    RIBBONFRIEND_FIELD_NUMBER: int
    RIBBONGROUP_FIELD_NUMBER: int
    DISPLAY_FIELD_NUMBER: int
    GRPMSGDISPLAY_FIELD_NUMBER: int
    OVER_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    GAMENICK_FIELD_NUMBER: int
    UNDECIDFORQIM_FIELD_NUMBER: int
    UNREADCOUNT3_FIELD_NUMBER: int
    HASSUSPICIOUSFLAG_FIELD_NUMBER: int
    @property
    def head(self) -> RspHead: ...
    unreadFriendCount: int
    unreadGroupCount: int
    latestFriendSeq: int
    latestGroupSeq: int
    followingFriendSeq: int
    followingGroupSeq: int
    @property
    def friendmsgs(self) -> RepeatedCompositeFieldContainer[StructMsg]: ...
    @property
    def groupmsgs(self) -> RepeatedCompositeFieldContainer[StructMsg]: ...
    @property
    def ribbonFriend(self) -> StructMsg: ...
    @property
    def ribbonGroup(self) -> StructMsg: ...
    display: Text
    grpMsgDisplay: Text
    over: int
    checktype: int
    gameNick: Text
    undecidForQim: bytes
    unReadCount3: int
    hasSuspiciousFlag: int
    def __init__(self,
        *,
        head: Optional[RspHead] = ...,
        unreadFriendCount: Optional[int] = ...,
        unreadGroupCount: Optional[int] = ...,
        latestFriendSeq: Optional[int] = ...,
        latestGroupSeq: Optional[int] = ...,
        followingFriendSeq: Optional[int] = ...,
        followingGroupSeq: Optional[int] = ...,
        friendmsgs: Optional[Iterable[StructMsg]] = ...,
        groupmsgs: Optional[Iterable[StructMsg]] = ...,
        ribbonFriend: Optional[StructMsg] = ...,
        ribbonGroup: Optional[StructMsg] = ...,
        display: Optional[Text] = ...,
        grpMsgDisplay: Optional[Text] = ...,
        over: Optional[int] = ...,
        checktype: Optional[int] = ...,
        gameNick: Optional[Text] = ...,
        undecidForQim: Optional[bytes] = ...,
        unReadCount3: Optional[int] = ...,
        hasSuspiciousFlag: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","display",b"display","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","gameNick",b"gameNick","grpMsgDisplay",b"grpMsgDisplay","hasSuspiciousFlag",b"hasSuspiciousFlag","head",b"head","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","over",b"over","ribbonFriend",b"ribbonFriend","ribbonGroup",b"ribbonGroup","unReadCount3",b"unReadCount3","undecidForQim",b"undecidForQim","unreadFriendCount",b"unreadFriendCount","unreadGroupCount",b"unreadGroupCount"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","display",b"display","followingFriendSeq",b"followingFriendSeq","followingGroupSeq",b"followingGroupSeq","friendmsgs",b"friendmsgs","gameNick",b"gameNick","groupmsgs",b"groupmsgs","grpMsgDisplay",b"grpMsgDisplay","hasSuspiciousFlag",b"hasSuspiciousFlag","head",b"head","latestFriendSeq",b"latestFriendSeq","latestGroupSeq",b"latestGroupSeq","over",b"over","ribbonFriend",b"ribbonFriend","ribbonGroup",b"ribbonGroup","unReadCount3",b"unReadCount3","undecidForQim",b"undecidForQim","unreadFriendCount",b"unreadFriendCount","unreadGroupCount",b"unreadGroupCount"]) -> None: ...

class RspSystemMsgRead(Message):
    DESCRIPTOR: Descriptor
    HEAD_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    CHECKTYPE_FIELD_NUMBER: int
    @property
    def head(self) -> RspHead: ...
    type: int
    checktype: int
    def __init__(self,
        *,
        head: Optional[RspHead] = ...,
        type: Optional[int] = ...,
        checktype: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["checktype",b"checktype","head",b"head","type",b"type"]) -> bool: ...
    def ClearField(self, field_name: Literal["checktype",b"checktype","head",b"head","type",b"type"]) -> None: ...

class StructMsg(Message):
    DESCRIPTOR: Descriptor
    VERSION_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    SEQ_FIELD_NUMBER: int
    TIME_FIELD_NUMBER: int
    REQUIN_FIELD_NUMBER: int
    UNREADFLAG_FIELD_NUMBER: int
    MSG_FIELD_NUMBER: int
    version: int
    type: int
    seq: int
    time: int
    reqUin: int
    unreadFlag: int
    @property
    def msg(self) -> SystemMsg: ...
    def __init__(self,
        *,
        version: Optional[int] = ...,
        type: Optional[int] = ...,
        seq: Optional[int] = ...,
        time: Optional[int] = ...,
        reqUin: Optional[int] = ...,
        unreadFlag: Optional[int] = ...,
        msg: Optional[SystemMsg] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["msg",b"msg","reqUin",b"reqUin","seq",b"seq","time",b"time","type",b"type","unreadFlag",b"unreadFlag","version",b"version"]) -> bool: ...
    def ClearField(self, field_name: Literal["msg",b"msg","reqUin",b"reqUin","seq",b"seq","time",b"time","type",b"type","unreadFlag",b"unreadFlag","version",b"version"]) -> None: ...

class SystemMsg(Message):
    DESCRIPTOR: Descriptor
    SUBTYPE_FIELD_NUMBER: int
    TITLE_FIELD_NUMBER: int
    DESCRIBE_FIELD_NUMBER: int
    ADDITIONAL_FIELD_NUMBER: int
    SOURCE_FIELD_NUMBER: int
    DECIDED_FIELD_NUMBER: int
    SRCID_FIELD_NUMBER: int
    SUBSRCID_FIELD_NUMBER: int
    ACTIONS_FIELD_NUMBER: int
    GROUPCODE_FIELD_NUMBER: int
    ACTIONUIN_FIELD_NUMBER: int
    GROUPMSGTYPE_FIELD_NUMBER: int
    GROUPINVITERROLE_FIELD_NUMBER: int
    FRIENDINFO_FIELD_NUMBER: int
    GROUPINFO_FIELD_NUMBER: int
    ACTORUIN_FIELD_NUMBER: int
    ACTORDESCRIBE_FIELD_NUMBER: int
    ADDITIONALLIST_FIELD_NUMBER: int
    RELATION_FIELD_NUMBER: int
    REQSUBTYPE_FIELD_NUMBER: int
    CLONEUIN_FIELD_NUMBER: int
    DISCUSSUIN_FIELD_NUMBER: int
    EIMGROUPID_FIELD_NUMBER: int
    INVITEEXTINFO_FIELD_NUMBER: int
    PAYGROUPEXTINFO_FIELD_NUMBER: int
    SOURCEFLAG_FIELD_NUMBER: int
    GAMENICK_FIELD_NUMBER: int
    GAMEMSG_FIELD_NUMBER: int
    GROUPFLAGEXT3_FIELD_NUMBER: int
    GROUPOWNERUIN_FIELD_NUMBER: int
    DOUBTFLAG_FIELD_NUMBER: int
    WARNINGTIPS_FIELD_NUMBER: int
    NAMEMORE_FIELD_NUMBER: int
    ADDTION_FIELD_NUMBER: int
    TRANSPARENTGROUPNOTIFY_FIELD_NUMBER: int
    REQUINFACEID_FIELD_NUMBER: int
    REQUINNICK_FIELD_NUMBER: int
    GROUPNAME_FIELD_NUMBER: int
    ACTIONUINNICK_FIELD_NUMBER: int
    QNA_FIELD_NUMBER: int
    DETAIL_FIELD_NUMBER: int
    GROUPEXTFLAG_FIELD_NUMBER: int
    ACTORUINNICK_FIELD_NUMBER: int
    PICURL_FIELD_NUMBER: int
    CLONEUINNICK_FIELD_NUMBER: int
    REQUINBUSINESSCARD_FIELD_NUMBER: int
    EIMGROUPIDNAME_FIELD_NUMBER: int
    REQUINPREREMARK_FIELD_NUMBER: int
    ACTIONUINQQNICK_FIELD_NUMBER: int
    ACTIONUINREMARK_FIELD_NUMBER: int
    REQUINGENDER_FIELD_NUMBER: int
    REQUINAGE_FIELD_NUMBER: int
    C2CINVITEJOINGROUPFLAG_FIELD_NUMBER: int
    CARDSWITCH_FIELD_NUMBER: int
    subType: int
    title: Text
    describe: Text
    additional: Text
    source: Text
    decided: Text
    srcId: int
    subSrcId: int
    @property
    def actions(self) -> RepeatedCompositeFieldContainer[SystemMsgAction]: ...
    groupCode: int
    actionUin: int
    groupMsgType: int
    groupInviterRole: int
    @property
    def friendInfo(self) -> FriendInfo: ...
    @property
    def groupInfo(self) -> GroupInfo: ...
    actorUin: int
    actorDescribe: Text
    additionalList: Text
    relation: int
    reqsubtype: int
    cloneUin: int
    discussUin: int
    eimGroupId: int
    @property
    def inviteExtinfo(self) -> MsgInviteExt: ...
    @property
    def payGroupExtinfo(self) -> MsgPayGroupExt: ...
    sourceFlag: int
    gameNick: bytes
    gameMsg: bytes
    groupFlagext3: int
    groupOwnerUin: int
    doubtFlag: int
    warningTips: bytes
    nameMore: bytes
    addtion: bytes
    transparentGroupNotify: bytes
    reqUinFaceid: int
    reqUinNick: Text
    groupName: Text
    actionUinNick: Text
    qna: Text
    detail: Text
    groupExtFlag: int
    actorUinNick: Text
    picUrl: bytes
    cloneUinNick: Text
    reqUinBusinessCard: bytes
    eimGroupIdName: bytes
    reqUinPreRemark: bytes
    actionUinQqNick: bytes
    actionUinRemark: bytes
    reqUinGender: int
    reqUinAge: int
    c2CInviteJoinGroupFlag: int
    cardSwitch: int
    def __init__(self,
        *,
        subType: Optional[int] = ...,
        title: Optional[Text] = ...,
        describe: Optional[Text] = ...,
        additional: Optional[Text] = ...,
        source: Optional[Text] = ...,
        decided: Optional[Text] = ...,
        srcId: Optional[int] = ...,
        subSrcId: Optional[int] = ...,
        actions: Optional[Iterable[SystemMsgAction]] = ...,
        groupCode: Optional[int] = ...,
        actionUin: Optional[int] = ...,
        groupMsgType: Optional[int] = ...,
        groupInviterRole: Optional[int] = ...,
        friendInfo: Optional[FriendInfo] = ...,
        groupInfo: Optional[GroupInfo] = ...,
        actorUin: Optional[int] = ...,
        actorDescribe: Optional[Text] = ...,
        additionalList: Optional[Text] = ...,
        relation: Optional[int] = ...,
        reqsubtype: Optional[int] = ...,
        cloneUin: Optional[int] = ...,
        discussUin: Optional[int] = ...,
        eimGroupId: Optional[int] = ...,
        inviteExtinfo: Optional[MsgInviteExt] = ...,
        payGroupExtinfo: Optional[MsgPayGroupExt] = ...,
        sourceFlag: Optional[int] = ...,
        gameNick: Optional[bytes] = ...,
        gameMsg: Optional[bytes] = ...,
        groupFlagext3: Optional[int] = ...,
        groupOwnerUin: Optional[int] = ...,
        doubtFlag: Optional[int] = ...,
        warningTips: Optional[bytes] = ...,
        nameMore: Optional[bytes] = ...,
        addtion: Optional[bytes] = ...,
        transparentGroupNotify: Optional[bytes] = ...,
        reqUinFaceid: Optional[int] = ...,
        reqUinNick: Optional[Text] = ...,
        groupName: Optional[Text] = ...,
        actionUinNick: Optional[Text] = ...,
        qna: Optional[Text] = ...,
        detail: Optional[Text] = ...,
        groupExtFlag: Optional[int] = ...,
        actorUinNick: Optional[Text] = ...,
        picUrl: Optional[bytes] = ...,
        cloneUinNick: Optional[Text] = ...,
        reqUinBusinessCard: Optional[bytes] = ...,
        eimGroupIdName: Optional[bytes] = ...,
        reqUinPreRemark: Optional[bytes] = ...,
        actionUinQqNick: Optional[bytes] = ...,
        actionUinRemark: Optional[bytes] = ...,
        reqUinGender: Optional[int] = ...,
        reqUinAge: Optional[int] = ...,
        c2CInviteJoinGroupFlag: Optional[int] = ...,
        cardSwitch: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["actionUin",b"actionUin","actionUinNick",b"actionUinNick","actionUinQqNick",b"actionUinQqNick","actionUinRemark",b"actionUinRemark","actorDescribe",b"actorDescribe","actorUin",b"actorUin","actorUinNick",b"actorUinNick","additional",b"additional","additionalList",b"additionalList","addtion",b"addtion","c2CInviteJoinGroupFlag",b"c2CInviteJoinGroupFlag","cardSwitch",b"cardSwitch","cloneUin",b"cloneUin","cloneUinNick",b"cloneUinNick","decided",b"decided","describe",b"describe","detail",b"detail","discussUin",b"discussUin","doubtFlag",b"doubtFlag","eimGroupId",b"eimGroupId","eimGroupIdName",b"eimGroupIdName","friendInfo",b"friendInfo","gameMsg",b"gameMsg","gameNick",b"gameNick","groupCode",b"groupCode","groupExtFlag",b"groupExtFlag","groupFlagext3",b"groupFlagext3","groupInfo",b"groupInfo","groupInviterRole",b"groupInviterRole","groupMsgType",b"groupMsgType","groupName",b"groupName","groupOwnerUin",b"groupOwnerUin","inviteExtinfo",b"inviteExtinfo","nameMore",b"nameMore","payGroupExtinfo",b"payGroupExtinfo","picUrl",b"picUrl","qna",b"qna","relation",b"relation","reqUinAge",b"reqUinAge","reqUinBusinessCard",b"reqUinBusinessCard","reqUinFaceid",b"reqUinFaceid","reqUinGender",b"reqUinGender","reqUinNick",b"reqUinNick","reqUinPreRemark",b"reqUinPreRemark","reqsubtype",b"reqsubtype","source",b"source","sourceFlag",b"sourceFlag","srcId",b"srcId","subSrcId",b"subSrcId","subType",b"subType","title",b"title","transparentGroupNotify",b"transparentGroupNotify","warningTips",b"warningTips"]) -> bool: ...
    def ClearField(self, field_name: Literal["actionUin",b"actionUin","actionUinNick",b"actionUinNick","actionUinQqNick",b"actionUinQqNick","actionUinRemark",b"actionUinRemark","actions",b"actions","actorDescribe",b"actorDescribe","actorUin",b"actorUin","actorUinNick",b"actorUinNick","additional",b"additional","additionalList",b"additionalList","addtion",b"addtion","c2CInviteJoinGroupFlag",b"c2CInviteJoinGroupFlag","cardSwitch",b"cardSwitch","cloneUin",b"cloneUin","cloneUinNick",b"cloneUinNick","decided",b"decided","describe",b"describe","detail",b"detail","discussUin",b"discussUin","doubtFlag",b"doubtFlag","eimGroupId",b"eimGroupId","eimGroupIdName",b"eimGroupIdName","friendInfo",b"friendInfo","gameMsg",b"gameMsg","gameNick",b"gameNick","groupCode",b"groupCode","groupExtFlag",b"groupExtFlag","groupFlagext3",b"groupFlagext3","groupInfo",b"groupInfo","groupInviterRole",b"groupInviterRole","groupMsgType",b"groupMsgType","groupName",b"groupName","groupOwnerUin",b"groupOwnerUin","inviteExtinfo",b"inviteExtinfo","nameMore",b"nameMore","payGroupExtinfo",b"payGroupExtinfo","picUrl",b"picUrl","qna",b"qna","relation",b"relation","reqUinAge",b"reqUinAge","reqUinBusinessCard",b"reqUinBusinessCard","reqUinFaceid",b"reqUinFaceid","reqUinGender",b"reqUinGender","reqUinNick",b"reqUinNick","reqUinPreRemark",b"reqUinPreRemark","reqsubtype",b"reqsubtype","source",b"source","sourceFlag",b"sourceFlag","srcId",b"srcId","subSrcId",b"subSrcId","subType",b"subType","title",b"title","transparentGroupNotify",b"transparentGroupNotify","warningTips",b"warningTips"]) -> None: ...

class SystemMsgAction(Message):
    DESCRIPTOR: Descriptor
    NAME_FIELD_NUMBER: int
    RESULT_FIELD_NUMBER: int
    ACTION_FIELD_NUMBER: int
    ACTIONINFO_FIELD_NUMBER: int
    DETAILNAME_FIELD_NUMBER: int
    name: Text
    result: Text
    action: int
    @property
    def actionInfo(self) -> SystemMsgActionInfo: ...
    detailName: Text
    def __init__(self,
        *,
        name: Optional[Text] = ...,
        result: Optional[Text] = ...,
        action: Optional[int] = ...,
        actionInfo: Optional[SystemMsgActionInfo] = ...,
        detailName: Optional[Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["action",b"action","actionInfo",b"actionInfo","detailName",b"detailName","name",b"name","result",b"result"]) -> bool: ...
    def ClearField(self, field_name: Literal["action",b"action","actionInfo",b"actionInfo","detailName",b"detailName","name",b"name","result",b"result"]) -> None: ...

class SystemMsgActionInfo(Message):
    DESCRIPTOR: Descriptor
    TYPE_FIELD_NUMBER: int
    GROUPCODE_FIELD_NUMBER: int
    SIG_FIELD_NUMBER: int
    MSG_FIELD_NUMBER: int
    GROUPID_FIELD_NUMBER: int
    REMARK_FIELD_NUMBER: int
    BLACKLIST_FIELD_NUMBER: int
    ADDFRDSNINFO_FIELD_NUMBER: int
    REQMSGTYPE_FIELD_NUMBER: int
    type: int
    groupCode: int
    sig: bytes
    msg: Text
    groupId: int
    remark: Text
    blacklist: bool
    @property
    def addFrdSNInfo(self) -> AddFrdSNInfo: ...
    reqMsgType: int
    def __init__(self,
        *,
        type: Optional[int] = ...,
        groupCode: Optional[int] = ...,
        sig: Optional[bytes] = ...,
        msg: Optional[Text] = ...,
        groupId: Optional[int] = ...,
        remark: Optional[Text] = ...,
        blacklist: Optional[bool] = ...,
        addFrdSNInfo: Optional[AddFrdSNInfo] = ...,
        reqMsgType: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["addFrdSNInfo",b"addFrdSNInfo","blacklist",b"blacklist","groupCode",b"groupCode","groupId",b"groupId","msg",b"msg","remark",b"remark","reqMsgType",b"reqMsgType","sig",b"sig","type",b"type"]) -> bool: ...
    def ClearField(self, field_name: Literal["addFrdSNInfo",b"addFrdSNInfo","blacklist",b"blacklist","groupCode",b"groupCode","groupId",b"groupId","msg",b"msg","remark",b"remark","reqMsgType",b"reqMsgType","sig",b"sig","type",b"type"]) -> None: ...
