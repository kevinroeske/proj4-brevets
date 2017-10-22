#test suite for brevet calculator
#
#Seven cases for each: an invalid (negative) distance, 0, a generic middle, and edge cases for the end.
#Note that I've set my calculator to just return the generic start time if the distance is invalid
#
#This one may be incomplete, but it tests the 200km brevet distance extensively
#
#
#
import acp_times
import arrow
#from acp_times import open_time(control_dist_km, brevet_dist_km, brevet_start_time)
#from acp_times import close_time(control_dist_km, brevet_dist_km, brevet_start_time)

testTwoHundred = [-5, 0, 100, 199, 200, 220, 221]
testThreeHundred = [-5, 0, 100, 299, 300, 330, 331]
testFourHundred = [-5, 0, 100, 399, 400, 440, 441]
testSixHundred = [-5, 0, 100, 599, 600, 660, 661]
testThousand = [-5, 0, 100, 999, 1000, 11000, 1101]

rsltTwo=['2017-01-01T00:00','2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltThr=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltFou=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltSix=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltTho=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']

def test_start_times():
    iterator = 0
    for i in testTwoHundred:
        test_value = arrow.get(acp_times.open_time(i, 200, '2017-01-01T00:00:00')).shift(hours=-8).isoformat()[:16]
        expected_value = arrow.get(rsltTwo[iterator]).isoformat()[:16]
        assert (test_value == expected_value)
        iterator+=1
        
    
