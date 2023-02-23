// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from rw_interfaces:msg/DetectionsVector.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "rw_interfaces/msg/detail/detections_vector__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace rw_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void DetectionsVector_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) rw_interfaces::msg::DetectionsVector(_init);
}

void DetectionsVector_fini_function(void * message_memory)
{
  auto typed_message = static_cast<rw_interfaces::msg::DetectionsVector *>(message_memory);
  typed_message->~DetectionsVector();
}

size_t size_function__DetectionsVector__distance(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<rw_interfaces::msg::Ultrasonic> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectionsVector__distance(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<rw_interfaces::msg::Ultrasonic> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectionsVector__distance(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<rw_interfaces::msg::Ultrasonic> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectionsVector__distance(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const rw_interfaces::msg::Ultrasonic *>(
    get_const_function__DetectionsVector__distance(untyped_member, index));
  auto & value = *reinterpret_cast<rw_interfaces::msg::Ultrasonic *>(untyped_value);
  value = item;
}

void assign_function__DetectionsVector__distance(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<rw_interfaces::msg::Ultrasonic *>(
    get_function__DetectionsVector__distance(untyped_member, index));
  const auto & value = *reinterpret_cast<const rw_interfaces::msg::Ultrasonic *>(untyped_value);
  item = value;
}

void resize_function__DetectionsVector__distance(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<rw_interfaces::msg::Ultrasonic> *>(untyped_member);
  member->resize(size);
}

size_t size_function__DetectionsVector__detection(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<irobot_create_msgs::msg::HazardDetection> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectionsVector__detection(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<irobot_create_msgs::msg::HazardDetection> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectionsVector__detection(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<irobot_create_msgs::msg::HazardDetection> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectionsVector__detection(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const irobot_create_msgs::msg::HazardDetection *>(
    get_const_function__DetectionsVector__detection(untyped_member, index));
  auto & value = *reinterpret_cast<irobot_create_msgs::msg::HazardDetection *>(untyped_value);
  value = item;
}

void assign_function__DetectionsVector__detection(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<irobot_create_msgs::msg::HazardDetection *>(
    get_function__DetectionsVector__detection(untyped_member, index));
  const auto & value = *reinterpret_cast<const irobot_create_msgs::msg::HazardDetection *>(untyped_value);
  item = value;
}

void resize_function__DetectionsVector__detection(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<irobot_create_msgs::msg::HazardDetection> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember DetectionsVector_message_member_array[3] = {
  {
    "distance",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<rw_interfaces::msg::Ultrasonic>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces::msg::DetectionsVector, distance),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectionsVector__distance,  // size() function pointer
    get_const_function__DetectionsVector__distance,  // get_const(index) function pointer
    get_function__DetectionsVector__distance,  // get(index) function pointer
    fetch_function__DetectionsVector__distance,  // fetch(index, &value) function pointer
    assign_function__DetectionsVector__distance,  // assign(index, value) function pointer
    resize_function__DetectionsVector__distance  // resize(index) function pointer
  },
  {
    "detection",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<irobot_create_msgs::msg::HazardDetection>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces::msg::DetectionsVector, detection),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectionsVector__detection,  // size() function pointer
    get_const_function__DetectionsVector__detection,  // get_const(index) function pointer
    get_function__DetectionsVector__detection,  // get(index) function pointer
    fetch_function__DetectionsVector__detection,  // fetch(index, &value) function pointer
    assign_function__DetectionsVector__detection,  // assign(index, value) function pointer
    resize_function__DetectionsVector__detection  // resize(index) function pointer
  },
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces::msg::DetectionsVector, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers DetectionsVector_message_members = {
  "rw_interfaces::msg",  // message namespace
  "DetectionsVector",  // message name
  3,  // number of fields
  sizeof(rw_interfaces::msg::DetectionsVector),
  DetectionsVector_message_member_array,  // message members
  DetectionsVector_init_function,  // function to initialize message memory (memory has to be allocated)
  DetectionsVector_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t DetectionsVector_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &DetectionsVector_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace rw_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<rw_interfaces::msg::DetectionsVector>()
{
  return &::rw_interfaces::msg::rosidl_typesupport_introspection_cpp::DetectionsVector_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, rw_interfaces, msg, DetectionsVector)() {
  return &::rw_interfaces::msg::rosidl_typesupport_introspection_cpp::DetectionsVector_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
