import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class VerifyResponse(_message.Message):
    __slots__ = ("identity", "access_token", "cost", "client_access_token")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identity: Identity
    access_token: AccessToken
    cost: int
    client_access_token: str
    def __init__(self, identity: _Optional[_Union[Identity, _Mapping]] = ..., access_token: _Optional[_Union[AccessToken, _Mapping]] = ..., cost: _Optional[int] = ..., client_access_token: _Optional[str] = ...) -> None: ...

class Identity(_message.Message):
    __slots__ = ("id", "phone", "email", "name", "picture", "created_at", "updated_at", "encrypted_phone", "phone_hash", "encrypted_email", "email_hash", "telegram_username", "telegram_id", "two_step_verification")
    ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PHONE_FIELD_NUMBER: _ClassVar[int]
    PHONE_HASH_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_HASH_FIELD_NUMBER: _ClassVar[int]
    TELEGRAM_USERNAME_FIELD_NUMBER: _ClassVar[int]
    TELEGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    TWO_STEP_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    phone: int
    email: str
    name: str
    picture: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    encrypted_phone: bytes
    phone_hash: bytes
    encrypted_email: bytes
    email_hash: bytes
    telegram_username: str
    telegram_id: int
    two_step_verification: bool
    def __init__(self, id: _Optional[int] = ..., phone: _Optional[int] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., picture: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., encrypted_phone: _Optional[bytes] = ..., phone_hash: _Optional[bytes] = ..., encrypted_email: _Optional[bytes] = ..., email_hash: _Optional[bytes] = ..., telegram_username: _Optional[str] = ..., telegram_id: _Optional[int] = ..., two_step_verification: bool = ...) -> None: ...

class AccessToken(_message.Message):
    __slots__ = ("id", "identity_id", "domain", "token", "phone_hash", "ip_address", "user_agent", "device_type", "two_step_verification", "expires_at", "created_at", "logout_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHONE_HASH_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TWO_STEP_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    identity_id: int
    domain: str
    token: int
    phone_hash: bytes
    ip_address: str
    user_agent: str
    device_type: str
    two_step_verification: bool
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    logout_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., identity_id: _Optional[int] = ..., domain: _Optional[str] = ..., token: _Optional[int] = ..., phone_hash: _Optional[bytes] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., device_type: _Optional[str] = ..., two_step_verification: bool = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., logout_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OtpRequest(_message.Message):
    __slots__ = ("id", "phone_hash", "ip_address", "domain", "token", "expires_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_HASH_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    phone_hash: bytes
    ip_address: str
    domain: str
    token: bytes
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., phone_hash: _Optional[bytes] = ..., ip_address: _Optional[str] = ..., domain: _Optional[str] = ..., token: _Optional[bytes] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Credential(_message.Message):
    __slots__ = ("id", "identity_id", "expires", "created", "token", "domain", "password_verified")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    id: int
    identity_id: int
    expires: int
    created: int
    token: int
    domain: str
    password_verified: bool
    def __init__(self, id: _Optional[int] = ..., identity_id: _Optional[int] = ..., expires: _Optional[int] = ..., created: _Optional[int] = ..., token: _Optional[int] = ..., domain: _Optional[str] = ..., password_verified: bool = ...) -> None: ...

class Password(_message.Message):
    __slots__ = ("id", "identity_id", "password", "expires_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    identity_id: int
    password: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., identity_id: _Optional[int] = ..., password: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WebhookEvent(_message.Message):
    __slots__ = ("timestamp", "logout_payload")
    class Logout(_message.Message):
        __slots__ = ("access_token_id",)
        ACCESS_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        access_token_id: int
        def __init__(self, access_token_id: _Optional[int] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    logout_payload: WebhookEvent.Logout
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., logout_payload: _Optional[_Union[WebhookEvent.Logout, _Mapping]] = ...) -> None: ...

class TemporaryAccessToken(_message.Message):
    __slots__ = ("credential", "expires_at")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
