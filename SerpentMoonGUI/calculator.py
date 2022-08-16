from datetime import datetime


def calculate_needed_points(current_level: int,
                            current_event_points: int,
                            event_ending: datetime = datetime(2022, 9, 26, 16, 0, 0),
                            date_to_compare: datetime = datetime.now()) -> float:
    """Calculates the minimum needed event points per day to successfully complete the Serpent Moon Event in
    Hunt: Showdown

    :param current_level: Current event level [technically the level you are working towards]
    :param current_event_points: Current collected event points in this bracket
    :param event_ending: Date of the Event ending [26. September 2022 16:00 by default]
    :param date_to_compare: Date to compare to [Current Date by default]
    :return: Daily amount of event points to finish the event in time
    """

    event_ending = event_ending
    days_remaining = (event_ending - date_to_compare).days

    # Generate all levels and corresponding point requirements
    event_levels = {i: (300 + (100 * i)) for i in range(1, 20)}

    # Calculate the remaining total needed event points
    remaining_total_event_points = 0
    for i in range(current_level, 20):
        remaining_total_event_points += event_levels[i]
    remaining_event_points = remaining_total_event_points - current_event_points
    needed_xp = round(remaining_event_points / days_remaining, 2)
    return needed_xp


def calculate_percentage_done(current_level: int,
                              current_event_points: int, ):
    event_levels = {i: (300 + (100 * i)) for i in range(1, 20)}
    max_event_points = sum(event_levels.values())
    collected_points = current_event_points
    for i in range(1, current_level + 1):
        collected_points += event_levels[i]

    return collected_points / max_event_points * 100
