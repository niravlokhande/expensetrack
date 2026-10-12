CREATE TABLE IF NOT EXISTS expenses (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    title      VARCHAR(100)  NOT NULL,
    amount     DECIMAL(10,2) NOT NULL,
    category   VARCHAR(50)   NOT NULL,
    created_at TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_amount_positive CHECK (amount > 0),
    INDEX idx_expenses_category (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO expenses (title, amount, category) VALUES
    ('Groceries', 45.50, 'Food'),
    ('Metro pass', 20.00, 'Transport');
