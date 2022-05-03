if __name__ == "__main__":
    N, M = map(int, input().split())
    lesson_list = list(map(int, input().split()))

    right = sum(lesson_list)
    left = max(lesson_list)
    while left <= right:

        mid = (left + right) // 2
        cnt = 0
        sum_lesson = 0
        for i in range(N):
            if sum_lesson + lesson_list[i] > mid:
                cnt += 1
                sum_lesson = 0

            sum_lesson += lesson_list[i]
        else:
            if sum_lesson:
                cnt += 1
        if cnt <= M:
            right = mid - 1
        elif cnt > M:
            left = mid + 1

    print(left)