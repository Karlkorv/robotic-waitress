// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from rw_interfaces:msg/Ultrasonic.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__ULTRASONIC__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define RW_INTERFACES__MSG__DETAIL__ULTRASONIC__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "rw_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "rw_interfaces/msg/detail/ultrasonic__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace rw_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rw_interfaces
cdr_serialize(
  const rw_interfaces::msg::Ultrasonic & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rw_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  rw_interfaces::msg::Ultrasonic & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rw_interfaces
get_serialized_size(
  const rw_interfaces::msg::Ultrasonic & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rw_interfaces
max_serialized_size_Ultrasonic(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace rw_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rw_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, rw_interfaces, msg, Ultrasonic)();

#ifdef __cplusplus
}
#endif

#endif  // RW_INTERFACES__MSG__DETAIL__ULTRASONIC__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
