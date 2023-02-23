// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rw_interfaces:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__DETECTIONS__BUILDER_HPP_
#define RW_INTERFACES__MSG__DETAIL__DETECTIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rw_interfaces/msg/detail/detections__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rw_interfaces
{

namespace msg
{

namespace builder
{

class Init_Detections_header
{
public:
  explicit Init_Detections_header(::rw_interfaces::msg::Detections & msg)
  : msg_(msg)
  {}
  ::rw_interfaces::msg::Detections header(::rw_interfaces::msg::Detections::_header_type arg)
  {
    msg_.header = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rw_interfaces::msg::Detections msg_;
};

class Init_Detections_detection
{
public:
  explicit Init_Detections_detection(::rw_interfaces::msg::Detections & msg)
  : msg_(msg)
  {}
  Init_Detections_header detection(::rw_interfaces::msg::Detections::_detection_type arg)
  {
    msg_.detection = std::move(arg);
    return Init_Detections_header(msg_);
  }

private:
  ::rw_interfaces::msg::Detections msg_;
};

class Init_Detections_distance
{
public:
  Init_Detections_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Detections_detection distance(::rw_interfaces::msg::Detections::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_Detections_detection(msg_);
  }

private:
  ::rw_interfaces::msg::Detections msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rw_interfaces::msg::Detections>()
{
  return rw_interfaces::msg::builder::Init_Detections_distance();
}

}  // namespace rw_interfaces

#endif  // RW_INTERFACES__MSG__DETAIL__DETECTIONS__BUILDER_HPP_
