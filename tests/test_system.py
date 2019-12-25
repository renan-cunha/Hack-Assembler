import pytest
import subprocess
import os
import filecmp


def test_add(tmpdir):
    main_path = os.path.join(__file__, "..", "../"
                             "main.py")
    main_path = os.path.abspath(main_path)
    add_path = os.path.join(__file__, "..",
                            "Add.asm")
    add_path = os.path.abspath(add_path)
    hack_path = os.path.join(__file__, "..",
                            "Add.hack")
    hack_path = os.path.abspath(hack_path)
    output_path = os.path.join(tmpdir, "Add.hack")
    subprocess.run(["python3", main_path, add_path, output_path])
    assert filecmp.cmp(hack_path, output_path)


def test_max_l(tmpdir):
    main_path = os.path.join(__file__, "..", "../"
                                             "main.py")
    main_path = os.path.abspath(main_path)
    add_path = os.path.join(__file__, "..",
                            "MaxL.asm")
    add_path = os.path.abspath(add_path)
    hack_path = os.path.join(__file__, "..",
                             "MaxL.hack")
    hack_path = os.path.abspath(hack_path)
    output_path = os.path.join(tmpdir, "MaxL.hack")
    subprocess.run(["python3", main_path, add_path, output_path])
    assert filecmp.cmp(hack_path, output_path)

def test_rect_l(tmpdir):
    main_path = os.path.join(__file__, "..", "../"
                                             "main.py")
    main_path = os.path.abspath(main_path)
    add_path = os.path.join(__file__, "..",
                            "RectL.asm")
    add_path = os.path.abspath(add_path)
    hack_path = os.path.join(__file__, "..",
                             "RectL.hack")
    hack_path = os.path.abspath(hack_path)
    output_path = os.path.join(tmpdir, "RecL.hack")
    subprocess.run(["python3", main_path, add_path, output_path])
    assert filecmp.cmp(hack_path, output_path)


def test_pong_l(tmpdir):
    main_path = os.path.join(__file__, "..", "../"
                                             "main.py")
    main_path = os.path.abspath(main_path)
    add_path = os.path.join(__file__, "..",
                            "PongL.asm")
    add_path = os.path.abspath(add_path)
    hack_path = os.path.join(__file__, "..",
                             "PongL.hack")
    hack_path = os.path.abspath(hack_path)
    output_path = os.path.join(tmpdir, "PongL.hack")
    subprocess.run(["python3", main_path, add_path, output_path])
    assert filecmp.cmp(hack_path, output_path)
