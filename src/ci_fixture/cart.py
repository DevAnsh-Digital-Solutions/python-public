from dataclasses import dataclass, field

from ci_fixture.multiply import multiply


@dataclass
class Cart:
    """A shopping cart of (unit price, quantity) lines."""

    lines: list[tuple[float, int]] = field(default_factory=list)

    def add_item(self, unit_price: float, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        self.lines.append((unit_price, quantity))

    def subtotal(self) -> float:
        return sum(multiply(price, qty) for price, qty in self.lines)

    def total(self, discount_pct: float = 0.0) -> float:
        if not 0 <= discount_pct <= 100:
            raise ValueError("discount_pct must be between 0 and 100")
        return self.subtotal() * (1 - discount_pct / 100)
