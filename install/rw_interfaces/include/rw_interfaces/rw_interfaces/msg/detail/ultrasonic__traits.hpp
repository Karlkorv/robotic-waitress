// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rw_interfaces:msg/Ultrasonic.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__ULTRASONIC__TRAITS_HPP_
#define RW_INTERFACES__MSG__DETAIL__ULTRASONIC__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "rw_interfaces/msg/detail/ultrasonic__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rw_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Ultrasonic & msg,
  std::ostream & out)
{
  out << "{";
  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << ", ";
  }

  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Ultrasonic & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }

  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Ultrasonic & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace rw_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use rw_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const rw_interfaces::msg::Ultrasonic & msg,
  std::ostream & out, size_t indentation = 0)
{
  rw_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use rw_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const rw_interfaces::msg::Ultrasonic & msg)
{
  return rw_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<rw_interfaces::msg::Ultrasonic>()
{
  return "rw_interfaces::msg::Ultrasonic";
}

template<>
inline const char * name<rw_interfaces::msg::Ultrasonic>()
{
  return "rw_interfaces/msg/Ultrasonic";
}

template<>
struct has_fixed_size<rw_interfaces::msg::Ultrasonic>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<rw_interfaces::msg::Ultrasonic>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<rw_interfaces::msg::Ultrasonic>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RW_INTERFACES__MSG__DETAIL__ULTRASONIC__TRAITS_HPP_
