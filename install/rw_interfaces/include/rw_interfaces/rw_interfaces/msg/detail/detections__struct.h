// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rw_interfaces:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__DETECTIONS__STRUCT_H_
#define RW_INTERFACES__MSG__DETAIL__DETECTIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'distance'
#include "rw_interfaces/msg/detail/ultrasonic__struct.h"
// Member 'detection'
#include "irobot_create_msgs/msg/detail/hazard_detection__struct.h"
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Detections in the package rw_interfaces.
typedef struct rw_interfaces__msg__Detections
{
  rw_interfaces__msg__Ultrasonic__Sequence distance;
  irobot_create_msgs__msg__HazardDetection__Sequence detection;
  std_msgs__msg__Header header;
} rw_interfaces__msg__Detections;

// Struct for a sequence of rw_interfaces__msg__Detections.
typedef struct rw_interfaces__msg__Detections__Sequence
{
  rw_interfaces__msg__Detections * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rw_interfaces__msg__Detections__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // RW_INTERFACES__MSG__DETAIL__DETECTIONS__STRUCT_H_
