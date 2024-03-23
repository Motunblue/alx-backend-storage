-- Create trigger to decrease items when an order is inserted
CREATE TRIGGER decrease_order_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
