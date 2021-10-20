INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
5,
1,
1,
90);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
6,
1,
1,
50);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
4,
2,
1,
100);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
2,
3,
10,
500);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
3,
3,
2,
500);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
9,
4,
2,
500);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
10,
4,
4,
600);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
8,
4,
2,
100);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
7,
5,
15,
1050);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
6,
5,
1,
50);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
4,
5,
1,
100);

INSERT INTO `banquet_order`.`ordered_items`
(
`item_id`,
`from_order_id`,
`items_amount`,
`total_price`)
VALUES
(
2,
6,
11,
550);

SELECT `ordered_items`.`ordered_items_id`,
    `ordered_items`.`item_id`,
    `ordered_items`.`from_order_id`,
    `ordered_items`.`items_amount`,
    `ordered_items`.`total_price`
FROM `banquet_order`.`ordered_items`;
