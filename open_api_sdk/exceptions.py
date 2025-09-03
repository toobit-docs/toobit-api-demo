"""
TooBit API Exception handling module
"""

from typing import Optional, Dict, Any


class TooBitException(Exception):
    """TooBit API base exception class"""
    
    def __init__(self, message: str, code: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        self.message = message
        self.code = code
        self.response = response or {}
        super().__init__(self.message)


class ConfigurationError(TooBitException):
    """ConfigurationError"""
    pass


class AuthenticationError(TooBitException):
    """Authentication error"""
    pass


class APIError(TooBitException):
    """API call error"""
    pass


class RateLimitError(TooBitException):
    """Rate limit error"""
    pass


class ValidationError(TooBitException):
    """Parameter validation error"""
    pass


class NetworkError(TooBitException):
    """Network error"""
    pass


class OrderError(TooBitException):
    """Order related error"""
    pass


# TooBit specific error code mapping
ERROR_CODE_MAP = {
    -1000: "Unknown error",
    -1001: "Internal error",
    -1002: "Service unavailable",
    -1003: "Timeout",
    -1004: "Request rejected",
    -1006: "Exception response",
    -1007: "Request Timeout",
    -1008: "Invalid request",
    -1009: "Invalid new order",
    -1010: "Invalid cancel order",
    -1011: "Invalid order",
    -1012: "Invalid trading pair",
    -1013: "Invalid quantity",
    -1014: "Invalid price",
    -1015: "Invalid time",
    -1016: "Invalid signature",
    -1017: "Invalid time Timestamp",
    -1018: "Invalid request size",
    -1019: "Invalid request",
    -1020: "Invalid request",
    -1021: "Invalid request",
    -1022: "Invalid request",
    -1023: "Invalid request",
    -1024: "Invalid request",
    -1025: "Invalid request",
    -1026: "Invalid request",
    -1027: "Invalid request",
    -1028: "Invalid request",
    -1029: "Invalid request",
    -1030: "Invalid request",
    -1031: "Invalid request",
    -1032: "Invalid request",
    -1033: "Invalid request",
    -1034: "Invalid request",
    -1035: "Invalid request",
    -1036: "Invalid request",
    -1037: "Invalid request",
    -1038: "Invalid request",
    -1039: "Invalid request",
    -1040: "Invalid request",
    -1041: "Invalid request",
    -1042: "Invalid request",
    -1043: "Invalid request",
    -1044: "Invalid request",
    -1045: "Invalid request",
    -1046: "Invalid request",
    -1047: "Invalid request",
    -1048: "Invalid request",
    -1049: "Invalid request",
    -1050: "Invalid request",
    -1051: "Invalid request",
    -1052: "Invalid request",
    -1053: "Invalid request",
    -1054: "Invalid request",
    -1055: "Invalid request",
    -1056: "Invalid request",
    -1057: "Invalid request",
    -1058: "Invalid request",
    -1059: "Invalid request",
    -1060: "Invalid request",
    -1061: "Invalid request",
    -1062: "Invalid request",
    -1063: "Invalid request",
    -1064: "Invalid request",
    -1065: "Invalid request",
    -1066: "Invalid request",
    -1067: "Invalid request",
    -1068: "Invalid request",
    -1069: "Invalid request",
    -1070: "Invalid request",
    -1071: "Invalid request",
    -1072: "Invalid request",
    -1073: "Invalid request",
    -1074: "Invalid request",
    -1075: "Invalid request",
    -1076: "Invalid request",
    -1077: "Invalid request",
    -1078: "Invalid request",
    -1079: "Invalid request",
    -1080: "Invalid request",
    -1081: "Invalid request",
    -1082: "Invalid request",
    -1083: "Invalid request",
    -1084: "Invalid request",
    -1085: "Invalid request",
    -1086: "Invalid request",
    -1087: "Invalid request",
    -1088: "Invalid request",
    -1089: "Invalid request",
    -1090: "Invalid request",
    -1091: "Invalid request",
    -1092: "Invalid request",
    -1093: "Invalid request",
    -1094: "Invalid request",
    -1095: "Invalid request",
    -1096: "Invalid request",
    -1097: "Invalid request",
    -1098: "Invalid request",
    -1099: "Invalid request",
    -1100: "Invalid request",
    -1101: "Invalid request",
    -1102: "Invalid request",
    -1103: "Invalid request",
    -1104: "Invalid request",
    -1105: "Invalid request",
    -1106: "Invalid request",
    -1107: "Invalid request",
    -1108: "Invalid request",
    -1109: "Invalid request",
    -1110: "Invalid request",
    -1111: "Invalid request",
    -1112: "Invalid request",
    -1113: "Invalid request",
    -1114: "Invalid request",
    -1115: "Invalid request",
    -1116: "Invalid request",
    -1117: "Invalid request",
    -1118: "Invalid request",
    -1119: "Invalid request",
    -1120: "Invalid request",
    -1121: "Invalid request",
    -1122: "Invalid request",
    -1123: "Invalid request",
    -1124: "Invalid request",
    -1125: "Invalid request",
    -1126: "Invalid request",
    -1127: "Invalid request",
    -1128: "Invalid request",
    -1129: "Invalid request",
    -1130: "Invalid request",
    -1131: "Invalid request",
    -1132: "Invalid request",
    -1133: "Invalid request",
    -1134: "Invalid request",
    -1135: "Invalid request",
    -1136: "Invalid request",
    -1137: "Invalid request",
    -1138: "Invalid request",
    -1139: "Invalid request",
    -1140: "Invalid request",
    -1141: "Invalid request",
    -1142: "Invalid request",
    -1143: "Order not found",
    -1144: "Order already locked",
    -1145: "Order does not support cancel",
    -1146: "Order Create Timeout",
    -1147: "Order Cancel Timeout",
    -1193: "Order quantity limit",
    -1194: "Market order prohibited",
    -1195: "Limit order price too low",
    -1196: "Limit order price too high",
    -1197: "Limit order buy price too high",
    -1198: "Limit order sell price too low",
    -1199: "Order buy quantity too small",
    -1200: "Order buy quantity too large",
    -1201: "Limit order sell price too high",
    -1202: "Order sell quantity too small",
    -1203: "Order sell quantity too large",
    -1206: "Order amount too large",
    -2010: "New order rejected",
    -2011: "Cancel order rejected",
    -2013: "Order does not exist",
    -2014: "API key format invalid",
    -2015: "API key rejected",
    -2016: "No trading window",
}


def get_error_message(code: int) -> str:
    """Get error information based on error code"""
    return ERROR_CODE_MAP.get(code, f"Unknown errorCode: {code}")


def raise_toobit_exception(code: int, message: str, response: Optional[Dict[str, Any]] = None):
    """Raise corresponding exception based on error code"""
    error_message = f"{get_error_message(code)}: {message}"
    
    # Print detailed error information
    print(f"Error Details: {error_message}")
    if response:
        print(f"Error response data: {response}")
    
    if code in [-1001, -1002, -1003, -1006, -1007]:
        raise NetworkError(error_message, code, response)
    elif code in [-1016, -2014, -2015]:
        raise AuthenticationError(error_message, code, response)
    elif code in [-1004, -1008, -1009, -1010, -1011, -1012, -1013, -1014, -1015, -1017, -1018]:
        raise ValidationError(error_message, code, response)
    elif code in [-1143, -1144, -1145, -1146, -1147, -1193, -1194, -1195, -1196, -1197, -1198, -1199, -1200, -1201, -1202, -1203, -1206, -2010, -2011, -2013, -2016]:
        raise OrderError(error_message, code, response)
    elif code == -1005:  # Rate limit
        raise RateLimitError(error_message, code, response)
    else:
        raise APIError(error_message, code, response) 