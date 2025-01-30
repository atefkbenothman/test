//! A simple Hello World library
//!
//! This crate provides a basic implementation of a Hello World function.
//!
//! # Usage
//!
//! Add this to your Cargo.toml:
//!
//! ```toml
//! [dependencies]
//! hello_world = "0.1.0"
//! ```
//!
//! Then in your code:
//!
//! ```rust
//! use hello_world::hello_world;
//!
//! fn main() {
//!     println!("{}", hello_world());
//! }
//! ```

pub fn hello_world() -> String {
    "Hello, World!".to_string()
}