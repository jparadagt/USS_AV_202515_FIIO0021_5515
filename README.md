# Overview

A Python-based order management system for a restaurant or café that handles different types of products (food and beverages) with dynamic pricing rules. The system implements object-oriented programming principles with inheritance and polymorphism to manage products, calculate prices with discounts/promotions, and generate order summaries for customers.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Design Pattern
The system follows an object-oriented architecture using inheritance and polymorphism:

- **Abstract Base Class**: `Producto` serves as the foundation for all product types, defining common properties (name, price) and enforcing implementation of price calculation through abstract methods
- **Specialized Product Classes**: `Alimento` and `Bebida` inherit from `Producto`, each implementing specific pricing logic and additional properties
- **Order Management**: `Pedido` class aggregates products and handles order calculations and display

## Pricing Strategy
The system implements a flexible pricing model:

- **Base Price Adjustment**: All products have their base price multiplied by 1.5 during initialization
- **Dynamic Discounts**: Each product type can apply specific discounts:
  - Vegan food items: 5% discount
  - Large beverages: 10% discount
- **Polymorphic Calculation**: Price calculation is handled through method overriding, allowing each product type to implement its own pricing rules

## Data Flow
1. Products are created with base information (name, price, specific attributes)
2. Products are added to orders through the `Pedido` class
3. Final prices are calculated dynamically when displaying order details
4. Order totals aggregate all individual product prices after discounts

## Error Handling
The system includes a `ProductoInvalido` class to handle invalid product selections, returning zero cost and a descriptive name for invalid entries.

# External Dependencies

This is a standalone Python application with no external dependencies beyond the Python standard library. The system uses:

- **abc module**: For abstract base class implementation
- **Built-in Python features**: String manipulation, mathematical operations, and basic I/O functions

No databases, web frameworks, or third-party libraries are currently integrated into the system.
