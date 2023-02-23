// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rw_interfaces:msg/DetectionsVector.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__BUILDER_HPP_
#define RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rw_interfaces/msg/detail/detections_vector__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rw_interfaces
{

namespace msg
{

namespace builder
{

class Init_DetectionsVector_header
{
public:
  explicit Init_DetectionsVector_header(::rw_interfaces::msg::DetectionsVector & msg)
  : msg_(msg)
  {}
  ::rw_interfaces::msg::DetectionsVector header(::rw_interfaces::msg::DetectionsVector::_header_type arg)
  {
    msg_.header = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rw_interfaces::msg::DetectionsVector msg_;
};

class Init_DetectionsVector_detection
{
public:
  explicit Init_DetectionsVector_detection(::rw_interfaces::msg::DetectionsVector & msg)
  : msg_(msg)
  {}
  Init_DetectionsVector_header detection(::rw_interfaces::msg::DetectionsVector::_detection_type arg)
  {
    msg_.detection = std::move(arg);
    return Init_DetectionsVector_header(msg_);
  }

private:
  ::rw_interfaces::msg::DetectionsVector msg_;
};

class Init_DetectionsVector_distance
{
public:
  Init_DetectionsVector_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectionsVector_detection distance(::rw_interfaces::msg::DetectionsVector::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_DetectionsVector_detection(msg_);
  }

private:
  ::rw_interfaces::msg::DetectionsVector msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rw_interfaces::msg::DetectionsVector>()
{
  return rw_interfaces::msg::builder::Init_DetectionsVector_distance();
}

}  // namespace rw_interfaces

#endif  // RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__BUILDER_HPP_
