//! Tests for the hello_world library

extern crate hello_world;

#[test]
fn test_hello_world() {
    assert_eq!(hello_world::hello_world(), "Hello, World!");
}