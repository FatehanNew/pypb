import datetime

from packets import dataModel_pb2 as _dataModel_pb2
from identities import identities_pb2 as _identities_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from utils.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Via(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[Via]
    SMS: _ClassVar[Via]
    FCM: _ClassVar[Via]
    EMAIL: _ClassVar[Via]
    DATABASE: _ClassVar[Via]
    CALL: _ClassVar[Via]
    WEBHOOK: _ClassVar[Via]

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ObjectType]
    DEVICE: _ClassVar[ObjectType]
    USER: _ClassVar[ObjectType]
    OPERATION: _ClassVar[ObjectType]
    WORKFLOW_TASK: _ClassVar[ObjectType]

class AreaEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AREA_EXIT: _ClassVar[AreaEventType]
    AREA_ENTER: _ClassVar[AreaEventType]

class AnalogEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANALOG_EQUAL: _ClassVar[AnalogEventType]
    ANALOG_RISE_ABOVE: _ClassVar[AnalogEventType]
    ANALOG_FALL_BELOW: _ClassVar[AnalogEventType]

class TriggerGate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_GATE_AND: _ClassVar[TriggerGate]
    TRIGGER_GATE_OR: _ClassVar[TriggerGate]
NONE: Via
SMS: Via
FCM: Via
EMAIL: Via
DATABASE: Via
CALL: Via
WEBHOOK: Via
UNKNOWN: ObjectType
DEVICE: ObjectType
USER: ObjectType
OPERATION: ObjectType
WORKFLOW_TASK: ObjectType
AREA_EXIT: AreaEventType
AREA_ENTER: AreaEventType
ANALOG_EQUAL: AnalogEventType
ANALOG_RISE_ABOVE: AnalogEventType
ANALOG_FALL_BELOW: AnalogEventType
TRIGGER_GATE_AND: TriggerGate
TRIGGER_GATE_OR: TriggerGate

class TestMessage(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class NotifyJob(_message.Message):
    __slots__ = ("id", "user_id", "retries", "priority", "notify", "via")
    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOW: _ClassVar[NotifyJob.Priority]
        MEDIUM: _ClassVar[NotifyJob.Priority]
        HIGH: _ClassVar[NotifyJob.Priority]
    LOW: NotifyJob.Priority
    MEDIUM: NotifyJob.Priority
    HIGH: NotifyJob.Priority
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    retries: int
    priority: NotifyJob.Priority
    notify: Notify
    via: _containers.RepeatedScalarFieldContainer[Via]
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., retries: _Optional[int] = ..., priority: _Optional[_Union[NotifyJob.Priority, str]] = ..., notify: _Optional[_Union[Notify, _Mapping]] = ..., via: _Optional[_Iterable[_Union[Via, str]]] = ...) -> None: ...

class UserDeviceAlert(_message.Message):
    __slots__ = ("id", "user_id", "device_id", "organization_id", "alert_id", "condition", "timing", "status", "format", "alert", "unit", "object_type", "object_id")
    class Condition(_message.Message):
        __slots__ = ("from_time", "to_time", "sound_id", "text", "value", "type")
        FROM_TIME_FIELD_NUMBER: _ClassVar[int]
        TO_TIME_FIELD_NUMBER: _ClassVar[int]
        SOUND_ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        from_time: str
        to_time: str
        sound_id: int
        text: str
        value: int
        type: _containers.RepeatedScalarFieldContainer[Via]
        def __init__(self, from_time: _Optional[str] = ..., to_time: _Optional[str] = ..., sound_id: _Optional[int] = ..., text: _Optional[str] = ..., value: _Optional[int] = ..., type: _Optional[_Iterable[_Union[Via, str]]] = ...) -> None: ...
    class ConditionList(_message.Message):
        __slots__ = ("condition",)
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        condition: _containers.RepeatedCompositeFieldContainer[UserDeviceAlert.Condition]
        def __init__(self, condition: _Optional[_Iterable[_Union[UserDeviceAlert.Condition, _Mapping]]] = ...) -> None: ...
    class ConditionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UserDeviceAlert.ConditionList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserDeviceAlert.ConditionList, _Mapping]] = ...) -> None: ...
    class TimingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UserDeviceAlert.ConditionList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserDeviceAlert.ConditionList, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    device_id: int
    organization_id: int
    alert_id: int
    condition: _containers.MessageMap[int, UserDeviceAlert.ConditionList]
    timing: _containers.MessageMap[int, UserDeviceAlert.ConditionList]
    status: bool
    format: str
    alert: _dataModel_pb2.Alert
    unit: str
    object_type: str
    object_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., device_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., alert_id: _Optional[int] = ..., condition: _Optional[_Mapping[int, UserDeviceAlert.ConditionList]] = ..., timing: _Optional[_Mapping[int, UserDeviceAlert.ConditionList]] = ..., status: bool = ..., format: _Optional[str] = ..., alert: _Optional[_Union[_dataModel_pb2.Alert, str]] = ..., unit: _Optional[str] = ..., object_type: _Optional[str] = ..., object_id: _Optional[int] = ...) -> None: ...

class UserDeviceAlertList(_message.Message):
    __slots__ = ("list",)
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[UserDeviceAlert]
    def __init__(self, list: _Optional[_Iterable[_Union[UserDeviceAlert, _Mapping]]] = ...) -> None: ...

class Notify(_message.Message):
    __slots__ = ("title", "body", "sound", "image", "icon", "receiver", "object_id", "object_type", "timestamp", "data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    sound: int
    image: str
    icon: str
    receiver: _identities_pb2.Receiver
    object_id: int
    object_type: ObjectType
    timestamp: _timestamp_pb2.Timestamp
    data: _containers.ScalarMap[str, str]
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., sound: _Optional[int] = ..., image: _Optional[str] = ..., icon: _Optional[str] = ..., receiver: _Optional[_Union[_identities_pb2.Receiver, _Mapping]] = ..., object_id: _Optional[int] = ..., object_type: _Optional[_Union[ObjectType, str]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ("uuid", "user_id", "object_id", "object_type", "title", "body", "alert_id", "alert", "via", "data", "image", "sound", "created_at", "read_at", "user_alert_id")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    user_id: int
    object_id: int
    object_type: ObjectType
    title: str
    body: str
    alert_id: int
    alert: _dataModel_pb2.Alert
    via: _containers.RepeatedScalarFieldContainer[Via]
    data: _containers.ScalarMap[str, str]
    image: str
    sound: int
    created_at: _timestamp_pb2.Timestamp
    read_at: _timestamp_pb2.Timestamp
    user_alert_id: int
    def __init__(self, uuid: _Optional[str] = ..., user_id: _Optional[int] = ..., object_id: _Optional[int] = ..., object_type: _Optional[_Union[ObjectType, str]] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., alert_id: _Optional[int] = ..., alert: _Optional[_Union[_dataModel_pb2.Alert, str]] = ..., via: _Optional[_Iterable[_Union[Via, str]]] = ..., data: _Optional[_Mapping[str, str]] = ..., image: _Optional[str] = ..., sound: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_alert_id: _Optional[int] = ...) -> None: ...

class AlertModel(_message.Message):
    __slots__ = ("id", "organization_id", "alert_id", "alert_type", "unit", "value", "message", "name", "min_value", "max_value", "picture", "created_by", "updated_by", "created_at", "updated_at", "object_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    alert_id: int
    alert_type: int
    unit: str
    value: int
    message: str
    name: str
    min_value: str
    max_value: str
    picture: str
    created_by: int
    updated_by: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    object_type: str
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., alert_id: _Optional[int] = ..., alert_type: _Optional[int] = ..., unit: _Optional[str] = ..., value: _Optional[int] = ..., message: _Optional[str] = ..., name: _Optional[str] = ..., min_value: _Optional[str] = ..., max_value: _Optional[str] = ..., picture: _Optional[str] = ..., created_by: _Optional[int] = ..., updated_by: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., object_type: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("id", "user_id", "device_id", "organization_id", "created_by", "name", "event_data", "status", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    device_id: int
    organization_id: int
    created_by: int
    name: str
    event_data: EventData
    status: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., device_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., name: _Optional[str] = ..., event_data: _Optional[_Union[EventData, _Mapping]] = ..., status: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EventList(_message.Message):
    __slots__ = ("total", "current_page", "last_page", "per_page", "events")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    total: int
    current_page: int
    last_page: int
    per_page: int
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, total: _Optional[int] = ..., current_page: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class EventTemplate(_message.Message):
    __slots__ = ("id", "organization_id", "created_by", "name", "event_data", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    created_by: int
    name: str
    event_data: EventData
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., name: _Optional[str] = ..., event_data: _Optional[_Union[EventData, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EventData(_message.Message):
    __slots__ = ("continuous", "blind_filter", "notify", "trigger_gate", "mute_mask", "event_modules", "via", "template_id")
    CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
    BLIND_FILTER_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GATE_FIELD_NUMBER: _ClassVar[int]
    MUTE_MASK_FIELD_NUMBER: _ClassVar[int]
    EVENT_MODULES_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    continuous: bool
    blind_filter: bool
    notify: AlertNotify
    trigger_gate: TriggerGate
    mute_mask: _containers.RepeatedCompositeFieldContainer[MuteMask]
    event_modules: _containers.RepeatedCompositeFieldContainer[EventModule]
    via: _containers.RepeatedScalarFieldContainer[Via]
    template_id: int
    def __init__(self, continuous: bool = ..., blind_filter: bool = ..., notify: _Optional[_Union[AlertNotify, _Mapping]] = ..., trigger_gate: _Optional[_Union[TriggerGate, str]] = ..., mute_mask: _Optional[_Iterable[_Union[MuteMask, _Mapping]]] = ..., event_modules: _Optional[_Iterable[_Union[EventModule, _Mapping]]] = ..., via: _Optional[_Iterable[_Union[Via, str]]] = ..., template_id: _Optional[int] = ...) -> None: ...

class MuteMask(_message.Message):
    __slots__ = ("day_of_month", "day_of_week", "from_seconds", "to_seconds")
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    FROM_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    day_of_month: int
    day_of_week: int
    from_seconds: int
    to_seconds: int
    def __init__(self, day_of_month: _Optional[int] = ..., day_of_week: _Optional[int] = ..., from_seconds: _Optional[int] = ..., to_seconds: _Optional[int] = ...) -> None: ...

class AlertNotify(_message.Message):
    __slots__ = ("title", "body", "sound", "image", "icon")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    sound: int
    image: str
    icon: str
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., sound: _Optional[int] = ..., image: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...

class AreaEvent(_message.Message):
    __slots__ = ("area_id", "event_type")
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    area_id: int
    event_type: AreaEventType
    def __init__(self, area_id: _Optional[int] = ..., event_type: _Optional[_Union[AreaEventType, str]] = ...) -> None: ...

class DigitalEvent(_message.Message):
    __slots__ = ("trigger", "io")
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    IO_FIELD_NUMBER: _ClassVar[int]
    trigger: bool
    io: str
    def __init__(self, trigger: bool = ..., io: _Optional[str] = ...) -> None: ...

class AnalogEvent(_message.Message):
    __slots__ = ("value", "io", "type", "tolerance_percent")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    value: float
    io: str
    type: AnalogEventType
    tolerance_percent: int
    def __init__(self, value: _Optional[float] = ..., io: _Optional[str] = ..., type: _Optional[_Union[AnalogEventType, str]] = ..., tolerance_percent: _Optional[int] = ...) -> None: ...

class FormulaEvent(_message.Message):
    __slots__ = ("formula",)
    FORMULA_FIELD_NUMBER: _ClassVar[int]
    formula: str
    def __init__(self, formula: _Optional[str] = ...) -> None: ...

class ProtocolEvent(_message.Message):
    __slots__ = ("alert",)
    ALERT_FIELD_NUMBER: _ClassVar[int]
    alert: _dataModel_pb2.Alert
    def __init__(self, alert: _Optional[_Union[_dataModel_pb2.Alert, str]] = ...) -> None: ...

class SpeedEvent(_message.Message):
    __slots__ = ("speed_limit",)
    SPEED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    speed_limit: int
    def __init__(self, speed_limit: _Optional[int] = ...) -> None: ...

class IgnitionEvent(_message.Message):
    __slots__ = ("ignition_on", "ignition_off")
    IGNITION_ON_FIELD_NUMBER: _ClassVar[int]
    IGNITION_OFF_FIELD_NUMBER: _ClassVar[int]
    ignition_on: bool
    ignition_off: bool
    def __init__(self, ignition_on: bool = ..., ignition_off: bool = ...) -> None: ...

class BatteryEvent(_message.Message):
    __slots__ = ("percent_below",)
    PERCENT_BELOW_FIELD_NUMBER: _ClassVar[int]
    percent_below: int
    def __init__(self, percent_below: _Optional[int] = ...) -> None: ...

class OfflineEvent(_message.Message):
    __slots__ = ("seconds",)
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    def __init__(self, seconds: _Optional[int] = ...) -> None: ...

class GpsEvent(_message.Message):
    __slots__ = ("satellites_below",)
    SATELLITES_BELOW_FIELD_NUMBER: _ClassVar[int]
    satellites_below: int
    def __init__(self, satellites_below: _Optional[int] = ...) -> None: ...

class GsmEvent(_message.Message):
    __slots__ = ("signal_below",)
    SIGNAL_BELOW_FIELD_NUMBER: _ClassVar[int]
    signal_below: int
    def __init__(self, signal_below: _Optional[int] = ...) -> None: ...

class EventModule(_message.Message):
    __slots__ = ("force_to_fill", "area_event", "digital_event", "analog_event", "formula_event", "protocol_event", "speed_event", "ignition_event", "battery_event", "offline_event", "gps_event", "gsm_event")
    FORCE_TO_FILL_FIELD_NUMBER: _ClassVar[int]
    AREA_EVENT_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_EVENT_FIELD_NUMBER: _ClassVar[int]
    ANALOG_EVENT_FIELD_NUMBER: _ClassVar[int]
    FORMULA_EVENT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_EVENT_FIELD_NUMBER: _ClassVar[int]
    SPEED_EVENT_FIELD_NUMBER: _ClassVar[int]
    IGNITION_EVENT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_EVENT_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_EVENT_FIELD_NUMBER: _ClassVar[int]
    GPS_EVENT_FIELD_NUMBER: _ClassVar[int]
    GSM_EVENT_FIELD_NUMBER: _ClassVar[int]
    force_to_fill: bool
    area_event: AreaEvent
    digital_event: DigitalEvent
    analog_event: AnalogEvent
    formula_event: FormulaEvent
    protocol_event: ProtocolEvent
    speed_event: SpeedEvent
    ignition_event: IgnitionEvent
    battery_event: BatteryEvent
    offline_event: OfflineEvent
    gps_event: GpsEvent
    gsm_event: GsmEvent
    def __init__(self, force_to_fill: bool = ..., area_event: _Optional[_Union[AreaEvent, _Mapping]] = ..., digital_event: _Optional[_Union[DigitalEvent, _Mapping]] = ..., analog_event: _Optional[_Union[AnalogEvent, _Mapping]] = ..., formula_event: _Optional[_Union[FormulaEvent, _Mapping]] = ..., protocol_event: _Optional[_Union[ProtocolEvent, _Mapping]] = ..., speed_event: _Optional[_Union[SpeedEvent, _Mapping]] = ..., ignition_event: _Optional[_Union[IgnitionEvent, _Mapping]] = ..., battery_event: _Optional[_Union[BatteryEvent, _Mapping]] = ..., offline_event: _Optional[_Union[OfflineEvent, _Mapping]] = ..., gps_event: _Optional[_Union[GpsEvent, _Mapping]] = ..., gsm_event: _Optional[_Union[GsmEvent, _Mapping]] = ...) -> None: ...

class IsRunningCache(_message.Message):
    __slots__ = ("is_running", "notified_at")
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    NOTIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    is_running: bool
    notified_at: int
    def __init__(self, is_running: bool = ..., notified_at: _Optional[int] = ...) -> None: ...
