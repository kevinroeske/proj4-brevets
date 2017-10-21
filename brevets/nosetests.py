#test suite for brevet calculator
import acp_times
import arrow
#from acp_times import open_time(control_dist_km, brevet_dist_km, brevet_start_time)
#from acp_times import close_time(control_dist_km, brevet_dist_km, brevet_start_time)

testTwoHundred = [-5, 0, 100, 199, 200, 220, 221]
testThreeHundred = [-5, 0, 100, 299, 300, 330, 331]
testFourHundred = [-5, 0, 100, 399, 400, 440, 441]
testSixHundred = [-5, 0, 100, 599, 600, 660, 661]
testThousand = [-5, 0, 100, 999, 1000, 11000, 1101]

rsltTwo=['2017-01-01T00:00:00','2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltThr=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltFou=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltSix=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']
rsltTho=['2017-01-01T00:00','2017-01-01T02:56','2017-01-01T05:51','2017-01-01T00:00','2017-01-01T05:52','2017-01-01T05:52','2017-01-01T00:00']

iterator = 0
for i in testTwoHundred:
    test_value = arrow.get(acp_times.open_time(i, 200, '2017-01-01T00:00:00')).shift(hours=-8).isoformat()
    expected_value = arrow.get(rsltTwo[iterator]).isoformat()
    print("Testing at distance " + str(i) + ':')
    print("Generated time: " + test_value[:16])
    print("Expected time: " + expected_value[:16])
    if test_value[:16] == expected_value[:16]:
        print("Test Passed")
    else:
        print("Test Failed")
    iterator+=1
    print("")
    
