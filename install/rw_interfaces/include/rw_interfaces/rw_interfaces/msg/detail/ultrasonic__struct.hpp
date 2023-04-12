// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from rw_interfaces:msg/Ultrasonic.idl
// generated code does not contain a copyright notice

#ifndef RW_INTERFACES__MSG__DETAIL__ULTRASONIC__STRUCT_HPP_
#define RW_INTERFACES__MSG__DETAIL__ULTRASONIC__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__rw_interfaces__msg__Ultrasonic __attribute__((deprecated))
#else
# define DEPRECATED__rw_interfaces__msg__Ultrasonic __declspec(deprecated)
#endif

namespace rw_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Ultrasonic_
{
  using Type = Ultrasonic_<ContainerAllocator>;

  explicit Ultrasonic_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->distances.begin(), this->distances.end(), 0.0f);
    }
  }

  explicit Ultrasonic_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : distances(_alloc),
    header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->distances.begin(), this->distances.end(), 0.0f);
    }
  }

  // field types and members
  using _distances_type =
    std::array<float, 3>;
  _distances_type distances;
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;

  // setters for named parameter idiom
  Type & set__distances(
    const std::array<float, 3> & _arg)
  {
    this->distances = _arg;
    return *this;
  }
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    rw_interfaces::msg::Ultrasonic_<ContainerAllocator> *;
  using ConstRawPtr =
    const rw_interfaces::msg::Ultrasonic_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      rw_interfaces::msg::Ultrasonic_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      rw_interfaces::msg::Ultrasonic_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__rw_interfaces__msg__Ultrasonic
    std::shared_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__rw_interfaces__msg__Ultrasonic
    std::shared_ptr<rw_interfaces::msg::Ultrasonic_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Ultrasonic_ & other) const
  {
    if (this->distances != other.distances) {
      return false;
    }
    if (this->header != other.header) {
      return false;
    }
    return true;
  }
  bool operator!=(const Ultrasonic_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Ultrasonic_

// alias to use template instance with default allocator
using Ultrasonic =
  rw_interfaces::msg::Ultrasonic_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace rw_interfaces

#endif  // RW_INTERFACES__MSG__DETAIL__ULTRASONIC__STRUCT_HPP_
