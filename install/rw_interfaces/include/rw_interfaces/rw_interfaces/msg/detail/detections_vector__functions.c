// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rw_interfaces:msg/DetectionsVector.idl
// generated code does not contain a copyright notice
#include "rw_interfaces/msg/detail/detections_vector__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `distance`
#include "rw_interfaces/msg/detail/ultrasonic__functions.h"
// Member `detection`
#include "irobot_create_msgs/msg/detail/hazard_detection__functions.h"
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
rw_interfaces__msg__DetectionsVector__init(rw_interfaces__msg__DetectionsVector * msg)
{
  if (!msg) {
    return false;
  }
  // distance
  if (!rw_interfaces__msg__Ultrasonic__Sequence__init(&msg->distance, 0)) {
    rw_interfaces__msg__DetectionsVector__fini(msg);
    return false;
  }
  // detection
  if (!irobot_create_msgs__msg__HazardDetection__Sequence__init(&msg->detection, 0)) {
    rw_interfaces__msg__DetectionsVector__fini(msg);
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    rw_interfaces__msg__DetectionsVector__fini(msg);
    return false;
  }
  return true;
}

void
rw_interfaces__msg__DetectionsVector__fini(rw_interfaces__msg__DetectionsVector * msg)
{
  if (!msg) {
    return;
  }
  // distance
  rw_interfaces__msg__Ultrasonic__Sequence__fini(&msg->distance);
  // detection
  irobot_create_msgs__msg__HazardDetection__Sequence__fini(&msg->detection);
  // header
  std_msgs__msg__Header__fini(&msg->header);
}

bool
rw_interfaces__msg__DetectionsVector__are_equal(const rw_interfaces__msg__DetectionsVector * lhs, const rw_interfaces__msg__DetectionsVector * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // distance
  if (!rw_interfaces__msg__Ultrasonic__Sequence__are_equal(
      &(lhs->distance), &(rhs->distance)))
  {
    return false;
  }
  // detection
  if (!irobot_create_msgs__msg__HazardDetection__Sequence__are_equal(
      &(lhs->detection), &(rhs->detection)))
  {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  return true;
}

bool
rw_interfaces__msg__DetectionsVector__copy(
  const rw_interfaces__msg__DetectionsVector * input,
  rw_interfaces__msg__DetectionsVector * output)
{
  if (!input || !output) {
    return false;
  }
  // distance
  if (!rw_interfaces__msg__Ultrasonic__Sequence__copy(
      &(input->distance), &(output->distance)))
  {
    return false;
  }
  // detection
  if (!irobot_create_msgs__msg__HazardDetection__Sequence__copy(
      &(input->detection), &(output->detection)))
  {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  return true;
}

rw_interfaces__msg__DetectionsVector *
rw_interfaces__msg__DetectionsVector__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rw_interfaces__msg__DetectionsVector * msg = (rw_interfaces__msg__DetectionsVector *)allocator.allocate(sizeof(rw_interfaces__msg__DetectionsVector), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rw_interfaces__msg__DetectionsVector));
  bool success = rw_interfaces__msg__DetectionsVector__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rw_interfaces__msg__DetectionsVector__destroy(rw_interfaces__msg__DetectionsVector * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rw_interfaces__msg__DetectionsVector__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rw_interfaces__msg__DetectionsVector__Sequence__init(rw_interfaces__msg__DetectionsVector__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rw_interfaces__msg__DetectionsVector * data = NULL;

  if (size) {
    data = (rw_interfaces__msg__DetectionsVector *)allocator.zero_allocate(size, sizeof(rw_interfaces__msg__DetectionsVector), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rw_interfaces__msg__DetectionsVector__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rw_interfaces__msg__DetectionsVector__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rw_interfaces__msg__DetectionsVector__Sequence__fini(rw_interfaces__msg__DetectionsVector__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rw_interfaces__msg__DetectionsVector__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rw_interfaces__msg__DetectionsVector__Sequence *
rw_interfaces__msg__DetectionsVector__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rw_interfaces__msg__DetectionsVector__Sequence * array = (rw_interfaces__msg__DetectionsVector__Sequence *)allocator.allocate(sizeof(rw_interfaces__msg__DetectionsVector__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rw_interfaces__msg__DetectionsVector__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rw_interfaces__msg__DetectionsVector__Sequence__destroy(rw_interfaces__msg__DetectionsVector__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rw_interfaces__msg__DetectionsVector__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rw_interfaces__msg__DetectionsVector__Sequence__are_equal(const rw_interfaces__msg__DetectionsVector__Sequence * lhs, const rw_interfaces__msg__DetectionsVector__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rw_interfaces__msg__DetectionsVector__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rw_interfaces__msg__DetectionsVector__Sequence__copy(
  const rw_interfaces__msg__DetectionsVector__Sequence * input,
  rw_interfaces__msg__DetectionsVector__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rw_interfaces__msg__DetectionsVector);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rw_interfaces__msg__DetectionsVector * data =
      (rw_interfaces__msg__DetectionsVector *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rw_interfaces__msg__DetectionsVector__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rw_interfaces__msg__DetectionsVector__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rw_interfaces__msg__DetectionsVector__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
