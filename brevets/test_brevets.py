#test suite for brevet calculator
#
#See comments for explanation of case choice
#Note that I've set my calculator to just return the generic start time if the distance is invalid
#
#
#
#
#
import acp_times
import arrow
tzvalue = 8 
brevet_start_time = '2017-01-01T00:00'

open_km = [300, 1000, 1000, 1000]          #for opening times, an arbitrary zero distance, and a couple of edge cases for 1000km
open_ctrl = [0, 999, 1000, 1100]            #this should demonstrate that the calculations are correct
open_expected = ['2017-01-01T00:00', '2017-01-02T09:03', '2017-01-02T09:05', '2017-01-02T09:05']

close_km = [600, 600, 1000, 1000, 1000]     #for close times, we do a zero again, then 650km checkpoints on 600 and 1000km brevets
close_ctrl = [0, 650, 650, 999, 1005]       #to be sure they're correct, then edge cases for 1000km
close_expected = ['2017-01-01T01:00', '2017-01-02T16:00', '2017-01-02T20:23', '2017-01-04T02:55', '2017-01-04T03:00']

def test_start_times():
    i = 0 
    for dist in open_km:
        test_value = arrow.get(acp_times.open_time(open_ctrl[i], open_km[i], brevet_start_time)).shift(hours=-tzvalue).isoformat()[:16]
        expected_value = open_expected[i]
        assert (test_value == expected_value)
        i += 1

def test_close_times():
    i = 0 
    for dist in close_km:
        test_value = arrow.get(acp_times.close_time(close_ctrl[i], close_km[i], brevet_start_time)).shift(hours=-tzvalue).isoformat()[:16]
        expected_value = close_expected[i]
        assert (test_value == expected_value)
        i += 1
