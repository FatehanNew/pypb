import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from notifies import notify_pb2 as _notify_pb2
from identities import identities_pb2 as _identities_pb2
from financial import financial_pb2 as _financial_pb2
from devices import devices_pb2 as _devices_pb2
from devices import maintenance_pb2 as _maintenance_pb2
from packets import messages_pb2 as _messages_pb2
from models import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageOnly(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UserPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_identities_pb2.User]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_identities_pb2.User, _Mapping]]] = ..., **kwargs) -> None: ...

class VersionCheck(_message.Message):
    __slots__ = ("status", "message", "current_version", "force_update", "partner_version", "user_version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_VERSION_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    current_version: str
    force_update: bool
    partner_version: str
    user_version: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., current_version: _Optional[str] = ..., force_update: bool = ..., partner_version: _Optional[str] = ..., user_version: _Optional[str] = ...) -> None: ...

class Me(_message.Message):
    __slots__ = ("user", "person", "currencies", "permissions", "device", "device_count")
    USER_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    user: _identities_pb2.User
    person: _containers.RepeatedCompositeFieldContainer[_identities_pb2.Person]
    currencies: _containers.RepeatedCompositeFieldContainer[_financial_pb2.Currency]
    permissions: _containers.RepeatedScalarFieldContainer[_identities_pb2.Permission]
    device: _devices_pb2.Device
    device_count: int
    def __init__(self, user: _Optional[_Union[_identities_pb2.User, _Mapping]] = ..., person: _Optional[_Iterable[_Union[_identities_pb2.Person, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_financial_pb2.Currency, _Mapping]]] = ..., permissions: _Optional[_Iterable[_Union[_identities_pb2.Permission, str]]] = ..., device: _Optional[_Union[_devices_pb2.Device, _Mapping]] = ..., device_count: _Optional[int] = ...) -> None: ...

class DevicePagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_devices_pb2.Device]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_devices_pb2.Device, _Mapping]]] = ..., **kwargs) -> None: ...

class Config(_message.Message):
    __slots__ = ("id", "organization_id", "created_by", "updated_by", "key", "value", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    created_by: int
    updated_by: int
    key: str
    value: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., updated_by: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConfigList(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[Config]
    def __init__(self, configs: _Optional[_Iterable[_Union[Config, _Mapping]]] = ...) -> None: ...

class TransactionPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ..., **kwargs) -> None: ...

class Transaction(_message.Message):
    __slots__ = ("id", "organization_id", "from_user_id", "created_by", "updated_by", "transaction_reason", "picture", "description", "from_currency_id", "to_currency_id", "price", "type", "created_at", "updated_at", "currency", "organization")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REASON_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FROM_CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    TO_CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    from_user_id: int
    created_by: int
    updated_by: int
    transaction_reason: str
    picture: str
    description: str
    from_currency_id: int
    to_currency_id: int
    price: str
    type: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    currency: _financial_pb2.Currency
    organization: _identities_pb2.Organization
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., from_user_id: _Optional[int] = ..., created_by: _Optional[int] = ..., updated_by: _Optional[int] = ..., transaction_reason: _Optional[str] = ..., picture: _Optional[str] = ..., description: _Optional[str] = ..., from_currency_id: _Optional[int] = ..., to_currency_id: _Optional[int] = ..., price: _Optional[str] = ..., type: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[_Union[_financial_pb2.Currency, _Mapping]] = ..., organization: _Optional[_Union[_identities_pb2.Organization, _Mapping]] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("name", "count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class Statistics(_message.Message):
    __slots__ = ("total", "read", "unread", "channels_used")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    UNREAD_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_USED_FIELD_NUMBER: _ClassVar[int]
    total: int
    read: int
    unread: int
    channels_used: _containers.RepeatedCompositeFieldContainer[Channel]
    def __init__(self, total: _Optional[int] = ..., read: _Optional[int] = ..., unread: _Optional[int] = ..., channels_used: _Optional[_Iterable[_Union[Channel, _Mapping]]] = ...) -> None: ...

class TopRepeatedNotification(_message.Message):
    __slots__ = ("title", "count")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    title: str
    count: int
    def __init__(self, title: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class NotificationFull(_message.Message):
    __slots__ = ("uuid", "user_id", "object_id", "object_type", "title", "body", "alert_id", "user_alert_id", "alert", "via", "image", "sound", "read_at", "created_at", "updated_at", "alert_model", "user_alert", "data", "channels")
    class RawData(_message.Message):
        __slots__ = ("latitude", "longitude", "area_id", "area_name", "device_id", "alert_value", "gps_time")
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        AREA_ID_FIELD_NUMBER: _ClassVar[int]
        AREA_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        ALERT_VALUE_FIELD_NUMBER: _ClassVar[int]
        GPS_TIME_FIELD_NUMBER: _ClassVar[int]
        latitude: float
        longitude: float
        area_id: int
        area_name: str
        device_id: int
        alert_value: int
        gps_time: _timestamp_pb2.Timestamp
        def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., area_id: _Optional[int] = ..., area_name: _Optional[str] = ..., device_id: _Optional[int] = ..., alert_value: _Optional[int] = ..., gps_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ALERT_MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_ALERT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    user_id: int
    object_id: int
    object_type: str
    title: str
    body: str
    alert_id: int
    user_alert_id: int
    alert: int
    via: _containers.RepeatedScalarFieldContainer[int]
    image: str
    sound: int
    read_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    alert_model: _notify_pb2.AlertModel
    user_alert: _notify_pb2.UserDeviceAlert
    data: NotificationFull.RawData
    channels: _containers.RepeatedCompositeFieldContainer[Channel]
    def __init__(self, uuid: _Optional[str] = ..., user_id: _Optional[int] = ..., object_id: _Optional[int] = ..., object_type: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., alert_id: _Optional[int] = ..., user_alert_id: _Optional[int] = ..., alert: _Optional[int] = ..., via: _Optional[_Iterable[int]] = ..., image: _Optional[str] = ..., sound: _Optional[int] = ..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., alert_model: _Optional[_Union[_notify_pb2.AlertModel, _Mapping]] = ..., user_alert: _Optional[_Union[_notify_pb2.UserDeviceAlert, _Mapping]] = ..., data: _Optional[_Union[NotificationFull.RawData, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[Channel, _Mapping]]] = ...) -> None: ...

class NotificationPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[NotificationFull]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[NotificationFull, _Mapping]]] = ..., **kwargs) -> None: ...

class SessionPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[Session, _Mapping]]] = ..., **kwargs) -> None: ...

class TrackerPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_devices_pb2.Tracker]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_devices_pb2.Tracker, _Mapping]]] = ..., **kwargs) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "tokenable_type", "tokenable_id", "name", "abilities", "fcm", "ip", "domain", "partner_id", "user_agent", "device_type", "last_used_at", "expires_at", "created_at", "updated_at", "current_session", "is_expired")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKENABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKENABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABILITIES_FIELD_NUMBER: _ClassVar[int]
    FCM_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    id: int
    tokenable_type: str
    tokenable_id: int
    name: str
    abilities: _containers.RepeatedScalarFieldContainer[str]
    fcm: str
    ip: str
    domain: str
    partner_id: int
    user_agent: str
    device_type: str
    last_used_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    current_session: bool
    is_expired: bool
    def __init__(self, id: _Optional[int] = ..., tokenable_type: _Optional[str] = ..., tokenable_id: _Optional[int] = ..., name: _Optional[str] = ..., abilities: _Optional[_Iterable[str]] = ..., fcm: _Optional[str] = ..., ip: _Optional[str] = ..., domain: _Optional[str] = ..., partner_id: _Optional[int] = ..., user_agent: _Optional[str] = ..., device_type: _Optional[str] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., current_session: bool = ..., is_expired: bool = ...) -> None: ...

class CommandPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_messages_pb2.CommandStruct]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_messages_pb2.CommandStruct, _Mapping]]] = ..., **kwargs) -> None: ...

class LiveLocationPagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_models_pb2.LiveLocation]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_models_pb2.LiveLocation, _Mapping]]] = ..., **kwargs) -> None: ...

class MaintenancePagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_maintenance_pb2.Maintenance]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_maintenance_pb2.Maintenance, _Mapping]]] = ..., **kwargs) -> None: ...

class ServicePagination(_message.Message):
    __slots__ = ("current_page", "first_page_url", "last_page_url", "next_page_url", "prev_page_url", "path", "last_page", "per_page", "to", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: str
    prev_page_url: str
    path: str
    last_page: int
    per_page: int
    to: int
    data: _containers.RepeatedCompositeFieldContainer[_maintenance_pb2.MaintenanceService]
    def __init__(self, current_page: _Optional[int] = ..., first_page_url: _Optional[str] = ..., last_page_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., prev_page_url: _Optional[str] = ..., path: _Optional[str] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., to: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_maintenance_pb2.MaintenanceService, _Mapping]]] = ..., **kwargs) -> None: ...
