from areas import area_pb2 as _area_pb2
from models import models_pb2 as _models_pb2
from devices import devices_pb2 as _devices_pb2
from devices import maintenance_pb2 as _maintenance_pb2
from financial import financial_pb2 as _financial_pb2
from services import repositories_pb2 as _repositories_pb2
from identities import identities_pb2 as _identities_pb2
from identities import authentication_pb2 as _authentication_pb2
from notifies import notify_pb2 as _notify_pb2
from packets import messages_pb2 as _messages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventTemplateShowRequest(_message.Message):
    __slots__ = ("event_template_id",)
    EVENT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    event_template_id: int
    def __init__(self, event_template_id: _Optional[int] = ...) -> None: ...

class EventShowRequest(_message.Message):
    __slots__ = ("event_id", "device_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    device_id: int
    def __init__(self, event_id: _Optional[int] = ..., device_id: _Optional[int] = ...) -> None: ...

class CommandActionShowRequest(_message.Message):
    __slots__ = ("command_action_id",)
    COMMAND_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    command_action_id: int
    def __init__(self, command_action_id: _Optional[int] = ...) -> None: ...

class SubscriptionMethodShowRequest(_message.Message):
    __slots__ = ("event_id", "device_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    device_id: int
    def __init__(self, event_id: _Optional[int] = ..., device_id: _Optional[int] = ...) -> None: ...

class SubscriptionMethodIndexRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EventTemplateDestroyRequest(_message.Message):
    __slots__ = ("event_id",)
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    def __init__(self, event_id: _Optional[int] = ...) -> None: ...

class EventTemplateDestroyResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class EventDestroyRequest(_message.Message):
    __slots__ = ("event_id", "device_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    device_id: int
    def __init__(self, event_id: _Optional[int] = ..., device_id: _Optional[int] = ...) -> None: ...

class EventDestroyResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class EventTemplateIndexResponse(_message.Message):
    __slots__ = ("current_page", "to", "last_page", "per_page", "cost", "total", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    to: int
    last_page: int
    per_page: int
    cost: int
    total: int
    data: _containers.RepeatedCompositeFieldContainer[_notify_pb2.EventTemplate]
    def __init__(self, current_page: _Optional[int] = ..., to: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., cost: _Optional[int] = ..., total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_notify_pb2.EventTemplate, _Mapping]]] = ..., **kwargs) -> None: ...

class EventTemplateIndexRequest(_message.Message):
    __slots__ = ("device_id", "disable_pagination", "search", "page", "page_size", "organization_id", "query_filter", "sort", "order")
    class QueryFilterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FilterScope
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FilterScope, _Mapping]] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    disable_pagination: bool
    search: str
    page: int
    page_size: int
    organization_id: int
    query_filter: _containers.MessageMap[str, FilterScope]
    sort: str
    order: str
    def __init__(self, device_id: _Optional[int] = ..., disable_pagination: bool = ..., search: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., organization_id: _Optional[int] = ..., query_filter: _Optional[_Mapping[str, FilterScope]] = ..., sort: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class EventIndexRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    def __init__(self, device_id: _Optional[int] = ...) -> None: ...

class EventIndexResponse(_message.Message):
    __slots__ = ("cost", "events")
    COST_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    cost: int
    events: _containers.RepeatedCompositeFieldContainer[_notify_pb2.Event]
    def __init__(self, cost: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_notify_pb2.Event, _Mapping]]] = ...) -> None: ...

class MaintenanceIndexRequest(_message.Message):
    __slots__ = ("device_id", "status")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    status: _containers.RepeatedScalarFieldContainer[_maintenance_pb2.MaintenanceStatus]
    def __init__(self, device_id: _Optional[int] = ..., status: _Optional[_Iterable[_Union[_maintenance_pb2.MaintenanceStatus, str]]] = ...) -> None: ...

class MaintenanceIndexResponse(_message.Message):
    __slots__ = ("device", "maintenance", "statistics", "cost")
    class MostUsed(_message.Message):
        __slots__ = ("count", "service")
        COUNT_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        count: int
        service: str
        def __init__(self, count: _Optional[int] = ..., service: _Optional[str] = ...) -> None: ...
    class Statistics(_message.Message):
        __slots__ = ("completed", "not_completed", "total", "most_used_services")
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        NOT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        MOST_USED_SERVICES_FIELD_NUMBER: _ClassVar[int]
        completed: int
        not_completed: int
        total: int
        most_used_services: _containers.RepeatedCompositeFieldContainer[MaintenanceIndexResponse.MostUsed]
        def __init__(self, completed: _Optional[int] = ..., not_completed: _Optional[int] = ..., total: _Optional[int] = ..., most_used_services: _Optional[_Iterable[_Union[MaintenanceIndexResponse.MostUsed, _Mapping]]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    device: _repositories_pb2.DeviceRepo
    maintenance: _containers.RepeatedCompositeFieldContainer[_maintenance_pb2.Maintenance]
    statistics: MaintenanceIndexResponse.Statistics
    cost: int
    def __init__(self, device: _Optional[_Union[_repositories_pb2.DeviceRepo, _Mapping]] = ..., maintenance: _Optional[_Iterable[_Union[_maintenance_pb2.Maintenance, _Mapping]]] = ..., statistics: _Optional[_Union[MaintenanceIndexResponse.Statistics, _Mapping]] = ..., cost: _Optional[int] = ...) -> None: ...

class AuthRequest(_message.Message):
    __slots__ = ("credential",)
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    credential: str
    def __init__(self, credential: _Optional[str] = ...) -> None: ...

class AuthResponse(_message.Message):
    __slots__ = ("identity", "access_token", "user_repo", "cost")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_REPO_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    identity: _authentication_pb2.Identity
    access_token: _authentication_pb2.AccessToken
    user_repo: _repositories_pb2.UserRepo
    cost: int
    def __init__(self, identity: _Optional[_Union[_authentication_pb2.Identity, _Mapping]] = ..., access_token: _Optional[_Union[_authentication_pb2.AccessToken, _Mapping]] = ..., user_repo: _Optional[_Union[_repositories_pb2.UserRepo, _Mapping]] = ..., cost: _Optional[int] = ...) -> None: ...

class IoRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    def __init__(self, device_id: _Optional[int] = ...) -> None: ...

class IoResponse(_message.Message):
    __slots__ = ("cost", "records", "ios")
    COST_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    IOS_FIELD_NUMBER: _ClassVar[int]
    cost: int
    records: int
    ios: _containers.RepeatedCompositeFieldContainer[_devices_pb2.SystemIo]
    def __init__(self, cost: _Optional[int] = ..., records: _Optional[int] = ..., ios: _Optional[_Iterable[_Union[_devices_pb2.SystemIo, _Mapping]]] = ...) -> None: ...

class ConfigRequest(_message.Message):
    __slots__ = ("domain", "partner_id", "include_security_config")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SECURITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    domain: str
    partner_id: int
    include_security_config: bool
    def __init__(self, domain: _Optional[str] = ..., partner_id: _Optional[int] = ..., include_security_config: bool = ...) -> None: ...

class ConfigResponse(_message.Message):
    __slots__ = ("cost", "records", "list", "app_design", "app_sec")
    class AppDesignConfig(_message.Message):
        __slots__ = ("app_name", "logo", "web_background", "primary_color", "app_logo", "goftino", "app_background", "address", "phone", "telegram", "primary_icon_color", "secondary_icon_color", "default_role_id", "enable_registration", "default_register_organization_id", "google_client_id", "telegram_bot_username", "main_domain", "favicon")
        APP_NAME_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        WEB_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        APP_LOGO_FIELD_NUMBER: _ClassVar[int]
        GOFTINO_FIELD_NUMBER: _ClassVar[int]
        APP_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        TELEGRAM_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_ICON_COLOR_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_ICON_COLOR_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
        ENABLE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_REGISTER_ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        TELEGRAM_BOT_USERNAME_FIELD_NUMBER: _ClassVar[int]
        MAIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        FAVICON_FIELD_NUMBER: _ClassVar[int]
        app_name: str
        logo: str
        web_background: str
        primary_color: str
        app_logo: str
        goftino: str
        app_background: str
        address: str
        phone: str
        telegram: str
        primary_icon_color: str
        secondary_icon_color: str
        default_role_id: str
        enable_registration: str
        default_register_organization_id: str
        google_client_id: str
        telegram_bot_username: str
        main_domain: str
        favicon: str
        def __init__(self, app_name: _Optional[str] = ..., logo: _Optional[str] = ..., web_background: _Optional[str] = ..., primary_color: _Optional[str] = ..., app_logo: _Optional[str] = ..., goftino: _Optional[str] = ..., app_background: _Optional[str] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ..., telegram: _Optional[str] = ..., primary_icon_color: _Optional[str] = ..., secondary_icon_color: _Optional[str] = ..., default_role_id: _Optional[str] = ..., enable_registration: _Optional[str] = ..., default_register_organization_id: _Optional[str] = ..., google_client_id: _Optional[str] = ..., telegram_bot_username: _Optional[str] = ..., main_domain: _Optional[str] = ..., favicon: _Optional[str] = ...) -> None: ...
    class AppSecConfig(_message.Message):
        __slots__ = ("max_logs", "max_sessions", "max_otp_tries", "min_password_length", "credential_expiration_days", "forced_two_step_verification", "google_client_secret", "telegram_bot_token")
        MAX_LOGS_FIELD_NUMBER: _ClassVar[int]
        MAX_SESSIONS_FIELD_NUMBER: _ClassVar[int]
        MAX_OTP_TRIES_FIELD_NUMBER: _ClassVar[int]
        MIN_PASSWORD_LENGTH_FIELD_NUMBER: _ClassVar[int]
        CREDENTIAL_EXPIRATION_DAYS_FIELD_NUMBER: _ClassVar[int]
        FORCED_TWO_STEP_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        TELEGRAM_BOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_logs: int
        max_sessions: int
        max_otp_tries: int
        min_password_length: int
        credential_expiration_days: int
        forced_two_step_verification: bool
        google_client_secret: str
        telegram_bot_token: str
        def __init__(self, max_logs: _Optional[int] = ..., max_sessions: _Optional[int] = ..., max_otp_tries: _Optional[int] = ..., min_password_length: _Optional[int] = ..., credential_expiration_days: _Optional[int] = ..., forced_two_step_verification: bool = ..., google_client_secret: _Optional[str] = ..., telegram_bot_token: _Optional[str] = ...) -> None: ...
    COST_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    APP_DESIGN_FIELD_NUMBER: _ClassVar[int]
    APP_SEC_FIELD_NUMBER: _ClassVar[int]
    cost: int
    records: int
    list: _containers.RepeatedCompositeFieldContainer[_models_pb2.Config]
    app_design: ConfigResponse.AppDesignConfig
    app_sec: ConfigResponse.AppSecConfig
    def __init__(self, cost: _Optional[int] = ..., records: _Optional[int] = ..., list: _Optional[_Iterable[_Union[_models_pb2.Config, _Mapping]]] = ..., app_design: _Optional[_Union[ConfigResponse.AppDesignConfig, _Mapping]] = ..., app_sec: _Optional[_Union[ConfigResponse.AppSecConfig, _Mapping]] = ...) -> None: ...

class UserRequest(_message.Message):
    __slots__ = ("disable_pagination", "page", "page_size", "organization_id", "search", "sort", "order", "query_filter")
    class QueryFilterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FilterScope
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FilterScope, _Mapping]] = ...) -> None: ...
    DISABLE_PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    disable_pagination: bool
    page: int
    page_size: int
    organization_id: int
    search: str
    sort: str
    order: str
    query_filter: _containers.MessageMap[str, FilterScope]
    def __init__(self, disable_pagination: bool = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., organization_id: _Optional[int] = ..., search: _Optional[str] = ..., sort: _Optional[str] = ..., order: _Optional[str] = ..., query_filter: _Optional[_Mapping[str, FilterScope]] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("current_page", "to", "last_page", "per_page", "cost", "total", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    to: int
    last_page: int
    per_page: int
    cost: int
    total: int
    data: _containers.RepeatedCompositeFieldContainer[_repositories_pb2.UserRepo]
    def __init__(self, current_page: _Optional[int] = ..., to: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., cost: _Optional[int] = ..., total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_repositories_pb2.UserRepo, _Mapping]]] = ..., **kwargs) -> None: ...

class DeviceRequest(_message.Message):
    __slots__ = ("disable_pagination", "page", "page_size", "organization_id", "tracker_id", "search", "include_device_status", "query_filter", "sort", "order")
    class QueryFilterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FilterScope
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FilterScope, _Mapping]] = ...) -> None: ...
    DISABLE_PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKER_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    disable_pagination: bool
    page: int
    page_size: int
    organization_id: int
    tracker_id: int
    search: str
    include_device_status: bool
    query_filter: _containers.MessageMap[str, FilterScope]
    sort: str
    order: str
    def __init__(self, disable_pagination: bool = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., organization_id: _Optional[int] = ..., tracker_id: _Optional[int] = ..., search: _Optional[str] = ..., include_device_status: bool = ..., query_filter: _Optional[_Mapping[str, FilterScope]] = ..., sort: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class DeviceResponse(_message.Message):
    __slots__ = ("current_page", "to", "last_page", "per_page", "cost", "total", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    to: int
    last_page: int
    per_page: int
    cost: int
    total: int
    data: _containers.RepeatedCompositeFieldContainer[_repositories_pb2.DeviceRepo]
    def __init__(self, current_page: _Optional[int] = ..., to: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., cost: _Optional[int] = ..., total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_repositories_pb2.DeviceRepo, _Mapping]]] = ..., **kwargs) -> None: ...

class DeviceShowRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeviceShowResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: _repositories_pb2.DeviceRepo
    def __init__(self, device: _Optional[_Union[_repositories_pb2.DeviceRepo, _Mapping]] = ...) -> None: ...

class MeRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    def __init__(self, device_id: _Optional[int] = ...) -> None: ...

class MeResponse(_message.Message):
    __slots__ = ("user", "person", "currencies", "permissions", "device", "device_count", "cost", "error_message")
    USER_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user: _identities_pb2.User
    person: _containers.RepeatedCompositeFieldContainer[_repositories_pb2.PersonRepo]
    currencies: _containers.RepeatedCompositeFieldContainer[_financial_pb2.Currency]
    permissions: _containers.RepeatedScalarFieldContainer[_identities_pb2.Permission]
    device: _repositories_pb2.DeviceRepo
    device_count: int
    cost: int
    error_message: str
    def __init__(self, user: _Optional[_Union[_identities_pb2.User, _Mapping]] = ..., person: _Optional[_Iterable[_Union[_repositories_pb2.PersonRepo, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_financial_pb2.Currency, _Mapping]]] = ..., permissions: _Optional[_Iterable[_Union[_identities_pb2.Permission, str]]] = ..., device: _Optional[_Union[_repositories_pb2.DeviceRepo, _Mapping]] = ..., device_count: _Optional[int] = ..., cost: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class AreaIndexRequest(_message.Message):
    __slots__ = ("disable_pagination", "page", "page_size", "organization_ids", "area_ids", "type", "search")
    DISABLE_PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    AREA_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    disable_pagination: bool
    page: int
    page_size: int
    organization_ids: _containers.RepeatedScalarFieldContainer[int]
    area_ids: _containers.RepeatedScalarFieldContainer[int]
    type: _containers.RepeatedScalarFieldContainer[_area_pb2.AreaType]
    search: str
    def __init__(self, disable_pagination: bool = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., organization_ids: _Optional[_Iterable[int]] = ..., area_ids: _Optional[_Iterable[int]] = ..., type: _Optional[_Iterable[_Union[_area_pb2.AreaType, str]]] = ..., search: _Optional[str] = ...) -> None: ...

class AreaIndexResponse(_message.Message):
    __slots__ = ("current_page", "to", "last_page", "per_page", "cost", "total", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    to: int
    last_page: int
    per_page: int
    cost: int
    total: int
    data: _containers.RepeatedCompositeFieldContainer[_area_pb2.Area]
    def __init__(self, current_page: _Optional[int] = ..., to: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., cost: _Optional[int] = ..., total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_area_pb2.Area, _Mapping]]] = ..., **kwargs) -> None: ...

class AlertAndNotifications(_message.Message):
    __slots__ = ("device_id", "page", "platform", "total", "last_page", "records", "cost", "alerts", "notifications")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    page: int
    platform: str
    total: int
    last_page: int
    records: int
    cost: int
    alerts: _containers.RepeatedCompositeFieldContainer[_notify_pb2.UserDeviceAlert]
    notifications: _containers.RepeatedCompositeFieldContainer[_notify_pb2.Notification]
    def __init__(self, device_id: _Optional[int] = ..., page: _Optional[int] = ..., platform: _Optional[str] = ..., total: _Optional[int] = ..., last_page: _Optional[int] = ..., records: _Optional[int] = ..., cost: _Optional[int] = ..., alerts: _Optional[_Iterable[_Union[_notify_pb2.UserDeviceAlert, _Mapping]]] = ..., notifications: _Optional[_Iterable[_Union[_notify_pb2.Notification, _Mapping]]] = ...) -> None: ...

class FilterConditions(_message.Message):
    __slots__ = ("filter_type", "type", "filter")
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter_type: str
    type: str
    filter: str
    def __init__(self, filter_type: _Optional[str] = ..., type: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class FilterScope(_message.Message):
    __slots__ = ("filter_type", "operator", "conditions", "filter", "date_from", "date_to", "type")
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    filter_type: str
    operator: str
    conditions: _containers.RepeatedCompositeFieldContainer[FilterConditions]
    filter: str
    date_from: str
    date_to: str
    type: str
    def __init__(self, filter_type: _Optional[str] = ..., operator: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[FilterConditions, _Mapping]]] = ..., filter: _Optional[str] = ..., date_from: _Optional[str] = ..., date_to: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class SubmitOrderResponse(_message.Message):
    __slots__ = ("devices", "order")
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_repositories_pb2.DeviceRepo]
    order: _financial_pb2.Order
    def __init__(self, devices: _Optional[_Iterable[_Union[_repositories_pb2.DeviceRepo, _Mapping]]] = ..., order: _Optional[_Union[_financial_pb2.Order, _Mapping]] = ...) -> None: ...

class CommandActionIndexRequest(_message.Message):
    __slots__ = ("disable_pagination", "page", "page_size", "query_filter", "sort", "order")
    class QueryFilterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FilterScope
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FilterScope, _Mapping]] = ...) -> None: ...
    DISABLE_PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    disable_pagination: bool
    page: int
    page_size: int
    query_filter: _containers.MessageMap[str, FilterScope]
    sort: str
    order: str
    def __init__(self, disable_pagination: bool = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., query_filter: _Optional[_Mapping[str, FilterScope]] = ..., sort: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class CommandActionIndexResponse(_message.Message):
    __slots__ = ("current_page", "to", "last_page", "per_page", "cost", "total", "data")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    to: int
    last_page: int
    per_page: int
    cost: int
    total: int
    data: _containers.RepeatedCompositeFieldContainer[_devices_pb2.CommandAction]
    def __init__(self, current_page: _Optional[int] = ..., to: _Optional[int] = ..., last_page: _Optional[int] = ..., per_page: _Optional[int] = ..., cost: _Optional[int] = ..., total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_devices_pb2.CommandAction, _Mapping]]] = ..., **kwargs) -> None: ...

class CommandActionShowResponse(_message.Message):
    __slots__ = ("command_action_id",)
    COMMAND_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    command_action_id: int
    def __init__(self, command_action_id: _Optional[int] = ...) -> None: ...

class CommandActionListRequest(_message.Message):
    __slots__ = ("tracker_id",)
    TRACKER_ID_FIELD_NUMBER: _ClassVar[int]
    tracker_id: int
    def __init__(self, tracker_id: _Optional[int] = ...) -> None: ...

class CommandActionModel(_message.Message):
    __slots__ = ("command_id", "tracker_id", "command_action_id", "command_name", "action_name", "action_description", "action_picture", "sms", "gprs")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_PICTURE_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    GPRS_FIELD_NUMBER: _ClassVar[int]
    command_id: int
    tracker_id: int
    command_action_id: int
    command_name: str
    action_name: str
    action_description: str
    action_picture: str
    sms: _messages_pb2.CommandFormat
    gprs: _messages_pb2.CommandFormat
    def __init__(self, command_id: _Optional[int] = ..., tracker_id: _Optional[int] = ..., command_action_id: _Optional[int] = ..., command_name: _Optional[str] = ..., action_name: _Optional[str] = ..., action_description: _Optional[str] = ..., action_picture: _Optional[str] = ..., sms: _Optional[_Union[_messages_pb2.CommandFormat, _Mapping]] = ..., gprs: _Optional[_Union[_messages_pb2.CommandFormat, _Mapping]] = ...) -> None: ...

class CommandActionListResponse(_message.Message):
    __slots__ = ("cost", "data")
    COST_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    cost: int
    data: _containers.RepeatedCompositeFieldContainer[CommandActionModel]
    def __init__(self, cost: _Optional[int] = ..., data: _Optional[_Iterable[_Union[CommandActionModel, _Mapping]]] = ...) -> None: ...
