# Hello World Rust Library

A simple Rust library that provides a Hello World function.

## Usage

Add this to your Cargo.toml:

```toml
[dependencies]
hello_world = "0.1.0"
```

Then in your code:

```rust
use hello_world::hello_world;

fn main() {
    println!("{}", hello_world());
}
```

## Testing

Run the tests with:

```bash
cargo test
```

## Implementation

The implementation is in `src/lib.rs` and provides a single function:

```rust
pub fn hello_world() -> String {
    "Hello, World!".to_string()
}
```

This function returns a String containing "Hello, World!".