from datetime import date


def main() -> None:
    return


def get_basho_start_date(year: int, month: int) -> str:
    first_of_month = date(year, month, 1).weekday()  # Mon = 0 ... Sun = 6
    start_date = 14 - first_of_month  # Latest possible start date is 14th corresponding to first day being Monday
    return date(year, month, start_date).strftime("%Y%m%d")


def get_basho_end_date(year: int, month: int) -> str:
    first_of_month = date(year, month, 1).weekday()  # Mon = 0 ... Sun = 6
    end_date = 29 - first_of_month  # Latest possible end date is 29th corresponding to first day being Monday
    return date(year, month, end_date).strftime("%Y%m%d")


def get_basho_period(year: int, month: int) -> str:
    start = get_basho_start_date(year, month)
    end = get_basho_end_date(year, month)
    return start + "-" + end


def get_year_basho_period(year) -> list[str]:
    return []


def get_current_year_basho_periods() -> list[str]:
    return []


if __name__ == "__main__":
    main()