#!/latex_to_text/sh

# Run the Python scripts on examples.
# Usage: Run '../latex_to_text/test.sh' from the examples directory.
# The script compares the original and new tex files. They should be essentially identical.

latex_to_text='../latex_to_text'

j=1
while [ "${j}" -le 3 ]
do
    printf '\n\n'
    echo "### Test ${j}."
    python3 "${latex_to_text}/latextotext.py" "test-0${j}.tex"
    cp "test-0${j}.txt" "test-new-0${j}.txt"
    python3 "${latex_to_text}/texttolatex.py" "test-new-0${j}.txt" "test-0${j}.dic"
    printf '\n\n\n'
    echo "### Differences for test ${j}:"
    diff "test-0${j}.tex" "test-new-0${j}.tex"
    echo '### Press [enter].'
    read
    j="$(( j + 1 ))"
done
