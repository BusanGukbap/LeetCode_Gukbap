from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration) -> int:
        def solve(start1, dur1, start2, dur2):
            # --- 전처리: 두 번째 카테고리를 startTime 기준 오름차순 정렬 ---
            rides2 = sorted(zip(start2, dur2))  # [(start, duration), ...]
            m = len(rides2)

            # --- prefix min of duration ---
            # pref_min_dur[i] = rides2[0..i] 중 가장 짧은 duration
            # 용도: startTime <= finish1인 놀이기구 중 duration이 최소인 것을 O(1)에 조회
            pref_min_dur = [0] * m
            pref_min_dur[0] = rides2[0][1]
            for i in range(1, m):
                pref_min_dur[i] = min(pref_min_dur[i - 1], rides2[i][1])

            # --- suffix min of finish time (start + duration) ---
            # suf_min_finish[i] = rides2[i..m-1] 중 가장 빠른 종료 시각
            # 용도: startTime > finish1인 놀이기구는 기다려야 하므로,
            #        종료 시각 = start + duration 자체가 최소인 것을 O(1)에 조회
            suf_min_finish = [0] * m
            suf_min_finish[-1] = rides2[-1][0] + rides2[-1][1]
            for i in range(m - 2, -1, -1):
                suf_min_finish[i] = min(rides2[i][0] + rides2[i][1], suf_min_finish[i + 1])

            # 이분 탐색용: 정렬된 startTime만 따로 추출
            starts2 = [r[0] for r in rides2]

            ans = inf
            # --- 첫 번째 카테고리의 모든 놀이기구를 순회 ---
            for s, d in zip(start1, dur1):
                f1 = s + d  # 첫 번째 놀이기구 종료 시각

                # 이분 탐색: starts2에서 f1 이하인 마지막 인덱스 찾기
                # bisect_right(starts2, f1) - 1 = startTime <= f1인 가장 오른쪽 위치
                mid = bisect_right(starts2, f1) - 1

                # 케이스 A: startTime <= f1 (이미 열려있음 → 바로 탑승)
                # 종료 시각 = f1 + (이 구간에서 가장 짧은 duration)
                if mid >= 0:
                    ans = min(ans, f1 + pref_min_dur[mid])

                # 케이스 B: startTime > f1 (아직 안 열림 → 기다려야 함)
                # 종료 시각 = start + duration (f1과 무관, 그 자체가 종료 시각)
                if mid + 1 < m:
                    ans = min(ans, suf_min_finish[mid + 1])

            return ans

        # 두 순서 모두 시도: 육상→수상, 수상→육상
        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration),
        )