// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rw_interfaces:msg/Ultrasonic.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__ULTRASONIC__BUILDER_HPP_
#define RW_INTERFACES__MSG__DETAIL__ULTRASONIC__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rw_interfaces/msg/detail/ultrasonic__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rw_interfaces
{

namespace msg
{

namespace builder
{

class Init_Ultrasonic_header
{
public:
  explicit Init_Ultrasonic_header(::rw_interfaces::msg::Ultrasonic & msg)
  : msg_(msg)
  {}
  ::rw_interfaces::msg::Ultrasonic header(::rw_interfaces::msg::Ultrasonic::_header_type arg)
  {
    msg_.header = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rw_interfaces::msg::Ultrasonic msg_;
};

class Init_Ultrasonic_distance
{
public:
  Init_Ultrasonic_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Ultrasonic_header distance(::rw_interfaces::msg::Ultrasonic::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_Ultrasonic_header(msg_);
  }

private:
  ::rw_interfaces::msg::Ultrasonic msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rw_interfaces::msg::Ultrasonic>()
{
  return rw_interfaces::msg::builder::Init_Ultrasonic_distance();
}

}  // namespace rw_interfaces

#endif  // RW_INTERFACES__MSG__DETAIL__ULTRASONIC__BUILDER_HPP_
