// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rw_interfaces:msg/DetectionsVector.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rw_interfaces/msg/detail/detections_vector__rosidl_typesupport_introspection_c.h"
#include "rw_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rw_interfaces/msg/detail/detections_vector__functions.h"
#include "rw_interfaces/msg/detail/detections_vector__struct.h"


// Include directives for member types
// Member `distance`
#include "rw_interfaces/msg/ultrasonic.h"
// Member `distance`
#include "rw_interfaces/msg/detail/ultrasonic__rosidl_typesupport_introspection_c.h"
// Member `detection`
#include "irobot_create_msgs/msg/hazard_detection.h"
// Member `detection`
#include "irobot_create_msgs/msg/detail/hazard_detection__rosidl_typesupport_introspection_c.h"
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rw_interfaces__msg__DetectionsVector__init(message_memory);
}

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_fini_function(void * message_memory)
{
  rw_interfaces__msg__DetectionsVector__fini(message_memory);
}

size_t rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__size_function__DetectionsVector__distance(
  const void * untyped_member)
{
  const rw_interfaces__msg__Ultrasonic__Sequence * member =
    (const rw_interfaces__msg__Ultrasonic__Sequence *)(untyped_member);
  return member->size;
}

const void * rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__distance(
  const void * untyped_member, size_t index)
{
  const rw_interfaces__msg__Ultrasonic__Sequence * member =
    (const rw_interfaces__msg__Ultrasonic__Sequence *)(untyped_member);
  return &member->data[index];
}

void * rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__distance(
  void * untyped_member, size_t index)
{
  rw_interfaces__msg__Ultrasonic__Sequence * member =
    (rw_interfaces__msg__Ultrasonic__Sequence *)(untyped_member);
  return &member->data[index];
}

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__fetch_function__DetectionsVector__distance(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rw_interfaces__msg__Ultrasonic * item =
    ((const rw_interfaces__msg__Ultrasonic *)
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__distance(untyped_member, index));
  rw_interfaces__msg__Ultrasonic * value =
    (rw_interfaces__msg__Ultrasonic *)(untyped_value);
  *value = *item;
}

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__assign_function__DetectionsVector__distance(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rw_interfaces__msg__Ultrasonic * item =
    ((rw_interfaces__msg__Ultrasonic *)
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__distance(untyped_member, index));
  const rw_interfaces__msg__Ultrasonic * value =
    (const rw_interfaces__msg__Ultrasonic *)(untyped_value);
  *item = *value;
}

bool rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__resize_function__DetectionsVector__distance(
  void * untyped_member, size_t size)
{
  rw_interfaces__msg__Ultrasonic__Sequence * member =
    (rw_interfaces__msg__Ultrasonic__Sequence *)(untyped_member);
  rw_interfaces__msg__Ultrasonic__Sequence__fini(member);
  return rw_interfaces__msg__Ultrasonic__Sequence__init(member, size);
}

size_t rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__size_function__DetectionsVector__detection(
  const void * untyped_member)
{
  const irobot_create_msgs__msg__HazardDetection__Sequence * member =
    (const irobot_create_msgs__msg__HazardDetection__Sequence *)(untyped_member);
  return member->size;
}

const void * rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__detection(
  const void * untyped_member, size_t index)
{
  const irobot_create_msgs__msg__HazardDetection__Sequence * member =
    (const irobot_create_msgs__msg__HazardDetection__Sequence *)(untyped_member);
  return &member->data[index];
}

void * rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__detection(
  void * untyped_member, size_t index)
{
  irobot_create_msgs__msg__HazardDetection__Sequence * member =
    (irobot_create_msgs__msg__HazardDetection__Sequence *)(untyped_member);
  return &member->data[index];
}

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__fetch_function__DetectionsVector__detection(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const irobot_create_msgs__msg__HazardDetection * item =
    ((const irobot_create_msgs__msg__HazardDetection *)
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__detection(untyped_member, index));
  irobot_create_msgs__msg__HazardDetection * value =
    (irobot_create_msgs__msg__HazardDetection *)(untyped_value);
  *value = *item;
}

void rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__assign_function__DetectionsVector__detection(
  void * untyped_member, size_t index, const void * untyped_value)
{
  irobot_create_msgs__msg__HazardDetection * item =
    ((irobot_create_msgs__msg__HazardDetection *)
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__detection(untyped_member, index));
  const irobot_create_msgs__msg__HazardDetection * value =
    (const irobot_create_msgs__msg__HazardDetection *)(untyped_value);
  *item = *value;
}

bool rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__resize_function__DetectionsVector__detection(
  void * untyped_member, size_t size)
{
  irobot_create_msgs__msg__HazardDetection__Sequence * member =
    (irobot_create_msgs__msg__HazardDetection__Sequence *)(untyped_member);
  irobot_create_msgs__msg__HazardDetection__Sequence__fini(member);
  return irobot_create_msgs__msg__HazardDetection__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_member_array[3] = {
  {
    "distance",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces__msg__DetectionsVector, distance),  // bytes offset in struct
    NULL,  // default value
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__size_function__DetectionsVector__distance,  // size() function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__distance,  // get_const(index) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__distance,  // get(index) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__fetch_function__DetectionsVector__distance,  // fetch(index, &value) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__assign_function__DetectionsVector__distance,  // assign(index, value) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__resize_function__DetectionsVector__distance  // resize(index) function pointer
  },
  {
    "detection",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces__msg__DetectionsVector, detection),  // bytes offset in struct
    NULL,  // default value
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__size_function__DetectionsVector__detection,  // size() function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_const_function__DetectionsVector__detection,  // get_const(index) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__get_function__DetectionsVector__detection,  // get(index) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__fetch_function__DetectionsVector__detection,  // fetch(index, &value) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__assign_function__DetectionsVector__detection,  // assign(index, value) function pointer
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__resize_function__DetectionsVector__detection  // resize(index) function pointer
  },
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rw_interfaces__msg__DetectionsVector, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_members = {
  "rw_interfaces__msg",  // message namespace
  "DetectionsVector",  // message name
  3,  // number of fields
  sizeof(rw_interfaces__msg__DetectionsVector),
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_member_array,  // message members
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_init_function,  // function to initialize message memory (memory has to be allocated)
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_type_support_handle = {
  0,
  &rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rw_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rw_interfaces, msg, DetectionsVector)() {
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rw_interfaces, msg, Ultrasonic)();
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, irobot_create_msgs, msg, HazardDetection)();
  rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_type_support_handle.typesupport_identifier) {
    rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &rw_interfaces__msg__DetectionsVector__rosidl_typesupport_introspection_c__DetectionsVector_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
