"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import logging
import flask

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
timezone_shift = 8      #this allows us to adjust the time shift due to arrow being timezone-aware. It reads everything as utc time but
                        #outputs based on local time zone. Huge pain, but this is a good workaround
app = flask.Flask(__name__)
max_times = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}
min_speeds = [15, 11.428]
max_speeds = [34, 32, 30, 28] 

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    hours_till_open = 0
    leg_one_dist = 0
    leg_two_dist = 0
    leg_three_dist = 0
    leg_four_dist = 0

    if (control_dist_km <= 0 or control_dist_km > brevet_dist_km*1.1):
        return arrow.get(brevet_start_time).shift(hours=+timezone_shift).isoformat()
    if (control_dist_km >= brevet_dist_km and control_dist_km <= brevet_dist_km*1.1):
        control_dist_km = brevet_dist_km
    
    if (control_dist_km >= 200):
        leg_one_dist = 200
    else:
        leg_one_dist = control_dist_km

    if (control_dist_km > 400):
        leg_two_dist = 200
    elif (control_dist_km > 200):
        leg_two_dist = control_dist_km - 200

    if (control_dist_km > 600):
        leg_three_dist = 200
        leg_four_dist = control_dist_km - 600
    elif (control_dist_km > 400):
        leg_three_dist = control_dist_km - 400
    
    hours_till_open = leg_one_dist/max_speeds[0] + leg_two_dist/max_speeds[1] + leg_three_dist/max_speeds[2] + leg_four_dist/max_speeds[3]
    
    opening_time =  arrow.get(brevet_start_time).shift(hours=+hours_till_open+timezone_shift)
    if (opening_time.second >= 30):
        opening_time = opening_time.shift(minutes=+1)
    return opening_time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    hours_till_close = 0 
    leg_one_dist = 0 
    leg_two_dist = 0 

    if (control_dist_km <= 0 or control_dist_km > brevet_dist_km*1.1): 
        return arrow.get(brevet_start_time).shift(hours=+timezone_shift+1).isoformat()

    if (control_dist_km >= brevet_dist_km and control_dist_km <= brevet_dist_km*1.1):
        return arrow.get(brevet_start_time).shift(hours=+max_times[brevet_dist_km]+timezone_shift).isoformat()
    
    if (control_dist_km >= 600):
        leg_one_dist = 600
        leg_two_dist = control_dist_km - 600
    else:
        leg_one_dist = control_dist_km

    hours_till_close = leg_one_dist/min_speeds[0] + leg_two_dist/min_speeds[1]
    closing_time =  arrow.get(brevet_start_time).shift(hours=+hours_till_close+timezone_shift)
    if (closing_time.second >= 30):
        closing_time = closing_time.shift(minutes=+1)
    return closing_time.isoformat()
