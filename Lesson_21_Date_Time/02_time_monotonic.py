import time


def demonstrate_time_difference():
    print("Simulating the difference between time.time() and time.monotonic()")

    # Record the start times using time.time() and time.monotonic()
    start_wall_clock = time.time()
    start_monotonic = time.monotonic_ns()

    # Simulate a delay, e.g., waiting for 2 seconds
    print("Waiting for 2 seconds...")
    time.sleep(2)

    # Record the end times
    end_wall_clock = time.time()
    end_monotonic = time.monotonic_ns()

    # Calculate elapsed time for both
    elapsed_wall_clock = end_wall_clock - start_wall_clock
    elapsed_monotonic = end_monotonic - start_monotonic

    print(f"Elapsed time using time.time(): {elapsed_wall_clock:.6f} seconds")
    print(f"Elapsed time using time.monotonic(): {elapsed_monotonic:.6f} seconds")

    # Now simulate a change in system time
    print("\nSimulating a system time adjustment...")
    print("Before adjusting system clock:")
    b_time = time.time()
    b_time_monotonic = time.monotonic()
    print(f"  time.time(): {b_time}")
    print(f"  time.monotonic(): {b_time_monotonic}")

    breakpoint()
    # sudo date -s "$(date -d 'now - 2 minutes' '+%Y-%m-%d %H:%M:%S')"
    # sudo chronyc -a makestep   # return NTP sync

    print("After adjusting system clock (manually):")
    a_time = time.time()
    a_time_monotonic = time.monotonic()
    print(f"  time.time(): {a_time} (may have changed)")
    print(f"  time.monotonic(): {a_time_monotonic} (remains unaffected)")
    ''
    print('=' * 50)
    print(f'Time diff: {a_time - b_time}')
    print(f'Time monotonic diff {a_time_monotonic - b_time_monotonic}')


# Call the function
if __name__ == "__main__":
    demonstrate_time_difference()
