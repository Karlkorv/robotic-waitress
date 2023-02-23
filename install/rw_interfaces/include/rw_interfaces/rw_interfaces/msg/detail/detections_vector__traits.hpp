// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rw_interfaces:msg/DetectionsVector.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__TRAITS_HPP_
#define RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "rw_interfaces/msg/detail/detections_vector__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'distance'
#include "rw_interfaces/msg/detail/ultrasonic__traits.hpp"
// Member 'detection'
#include "irobot_create_msgs/msg/detail/hazard_detection__traits.hpp"
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rw_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const DetectionsVector & msg,
  std::ostream & out)
{
  out << "{";
  // member: distance
  {
    if (msg.distance.size() == 0) {
      out << "distance: []";
    } else {
      out << "distance: [";
      size_t pending_items = msg.distance.size();
      for (auto item : msg.distance) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: detection
  {
    if (msg.detection.size() == 0) {
      out << "detection: []";
    } else {
      out << "detection: [";
      size_t pending_items = msg.detection.size();
      for (auto item : msg.detection) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
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
  const DetectionsVector & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.distance.size() == 0) {
      out << "distance: []\n";
    } else {
      out << "distance:\n";
      for (auto item : msg.distance) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: detection
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.detection.size() == 0) {
      out << "detection: []\n";
    } else {
      out << "detection:\n";
      for (auto item : msg.detection) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
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

inline std::string to_yaml(const DetectionsVector & msg, bool use_flow_style = false)
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
  const rw_interfaces::msg::DetectionsVector & msg,
  std::ostream & out, size_t indentation = 0)
{
  rw_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use rw_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const rw_interfaces::msg::DetectionsVector & msg)
{
  return rw_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<rw_interfaces::msg::DetectionsVector>()
{
  return "rw_interfaces::msg::DetectionsVector";
}

template<>
inline const char * name<rw_interfaces::msg::DetectionsVector>()
{
  return "rw_interfaces/msg/DetectionsVector";
}

template<>
struct has_fixed_size<rw_interfaces::msg::DetectionsVector>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<rw_interfaces::msg::DetectionsVector>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<rw_interfaces::msg::DetectionsVector>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RW_INTERFACES__MSG__DETAIL__DETECTIONS_VECTOR__TRAITS_HPP_
