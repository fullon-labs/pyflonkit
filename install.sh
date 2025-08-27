pushd dist
python3 -m pip uninstall pyflonkit -y;python3 -m pip install ./pyflonkit-*.whl
popd
