def float_range(start, end):
    repeat = int((end - start) * 10)
    array = [start]
    for i in range(repeat):
        start = round(start + 0.1, 1)
        array.append(start)
    return array


teeth_dict = {'М': {7: list(range(6, 12)),
                    8: list(range(9, 14)),
                    9: list(range(10, 17)),
                    10: list(range(11, 20)),
                    11: list(range(14, 26)),
                    12: list(range(20, 40))
                    },
              'Ж': {7: list(range(6, 12)),
                    8: list(range(9, 14)),
                    9: list(range(11, 17)),
                    10: list(range(20, 40))
                    }
              }

bio_points_girls = {'Ma0': 0,
                    'Ma1': 1.2,
                    'Ma2': 2.4,
                    'Ma3': 3.6,
                    'P0': 0,
                    'P1': 0.3,
                    'P2': 0.6,
                    'P3': 0.9,
                    'Ax0': 0,
                    'Ax1': 0.4,
                    'Ax2': 0.8,
                    'Ax3': 1.2,
                    'Me0': 0,
                    'Me1': 2.1,
                    'Me2': 4.2,
                    'Me3': 6.3
                    }

bio_scale_girls = {10: [x for x in float_range(0, 1.1)],
                   11: [x for x in float_range(0, 1.8)],
                   12: [x for x in float_range(1.5, 3.7)],
                   13: [x for x in float_range(3.8, 12)],
                   14: [x for x in float_range(10.4, 12)],
                   15: [x for x in float_range(12, 12.2)],
                   16: [x for x in float_range(12, 12.2)],
                   17: [x for x in float_range(12, 12.2)],
                   }

bio_points_boys = {'Ax0': 0,
                   'Ax1': 1,
                   'Ax2': 2,
                   'Ax3': 3,
                   'Ax4': 4,
                   'P0': 0.0,
                   'P1': 1.1,
                   'P2': 2.2,
                   'P3': 3.3,
                   'P4': 4.4,
                   'P5': 5.5,
                   'L0': 0,
                   'L1': 0.6,
                   'L2': 1.2,
                   'V0': 0,
                   'V1': 0.7,
                   'V2': 1.4,
                   'F0': 0,
                   'F1': 1.6,
                   'F2': 3.2,
                   'F3': 4.8,
                   'F4': 6.4,
                   'F5': 8
                   }

bio_scale_boys = {12: [x for x in float_range(0, 0.7)],
                  13: [x for x in float_range(0, 4.5)],
                  14: [x for x in float_range(4.5, 12.6)],
                  15: [x for x in float_range(7.6, 14.2)],
                  16: [x for x in float_range(10.5, 15.3)],
                  17: [x for x in float_range(12.6, 20.3)],
                  }
