@echo off
setlocal enabledelayedexpansion
REM Batch script to execute all test cases with all implemented algorithms
REM Outputs results in a Markdown-style table for easy reading or redirection

:: List of problem files
set "TESTS=test1_simple_cycle.txt test2_priority_trap_cycle.txt test3_undirected_cycle.txt test4_local_max_min_trap.txt test5_cost_trap.txt test6_complex_multigoal_trap.txt test7_disconnected_graph.txt test8_start_is_goal.txt test9_all_else_equal.txt test10_complex_map.txt"

:: Algorithms
set "METHODS=DFS BFS GBFS AS CUS1 CUS2"

:: Header for Markdown table
echo ^| Filename ^| Method ^| Goal ^| Nodes ^| Path ^|
echo ^|----------^|--------^|------^|-------^|------^|

for %%F in (%TESTS%) do (
    for %%M in (%METHODS%) do (
        set "line1="
        set "line2="
        set "line3="
        REM Run the search and capture exactly the three lines of output
        for /f "tokens=* delims=" %%A in ('python search.py %%F %%M') do (
            REM Output lines directly after the header; line order is known
            if not defined line1 (
                set "line1=%%A"
            ) else if not defined line2 (
                set "line2=%%A"
            ) else if not defined line3 (
                set "line3=%%A"
                REM Print a table row using the captured lines
                call :printrow "%%F" "%%M" "!line1!" "!line2!" "!line3!"
                set "line1="
                set "line2="
                set "line3="
            )
        )
    )
)

goto :eof

:printrow
REM 1=filename,2=method,3=line1,4=line2,5=line3
setlocal enabledelayedexpansion
set "file=%~1"
set "method=%~2"
set "l1=%~3"
set "l2=%~4"
set "l3=%~5"

:: l1 contains "filename method"
:: l2 contains "goal nodes"
:: l3 contains path
for /f "tokens=1,2" %%G in ("!l2!") do (
    set "goal=%%G"
    set "nodes=%%H"
)
echo ^| !file! ^| !method! ^| !goal! ^| !nodes! ^| !l3! ^|
endlocal
goto :eof