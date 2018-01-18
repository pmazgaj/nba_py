from nba_py import league
try:
    # python 2 compatability
    from future_builtins import filter
except ImportError:
    pass


class TestPlayerSpeedDistanceTracking:
    def test_overall(self):
        speed = league.PlayerSpeedDistanceTracking(date_from='03/05/2016',
                                                   date_to='03/05/2016', season="2015-16")
        assert speed
        overall = speed.overall()
        assert overall
        iterator = filter(lambda d: d['PLAYER_NAME'] == 'Derrick Rose', overall)
        stats = next(iterator)
        assert stats
        assertions = {
            stats['GP']: 1, stats['MIN']: 29.25, stats['DIST_MILES']: 2.24,
            stats['DIST_FEET']: 11827.0, stats['DIST_MILES_OFF']: 1.29, stats['DIST_MILES_DEF']: 0.95,
            stats['AVG_SPEED']: 4.52, stats['AVG_SPEED_OFF']: 4.94, stats['AVG_SPEED_DEF']:  4.42
        }
        for assertion in assertions:
            assert assertion == assertions[assertion]