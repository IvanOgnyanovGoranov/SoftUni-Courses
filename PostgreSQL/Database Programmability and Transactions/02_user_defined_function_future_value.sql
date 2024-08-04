CREATE OR REPLACE FUNCTION fn_calculate_future_value 
    (initial_sum NUMERIC, 
    yearly_interest_rate NUMERIC,
    number_of_years INT)
RETURNS NUMERIC
AS
$$
DECLARE future_value NUMERIC;
BEGIN
    future_value := initial_sum * POWER((1 + yearly_interest_rate), number_of_years);
    RETURN future_value;
END;
$$
LANGUAGE plpgsql;