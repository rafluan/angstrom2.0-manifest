import os
import sys

if os.geteuid() == 0:
    print("ERROR: do not use the BSP as root. Exiting...")
    sys.exit(1)

def usage():
    print("\nUsage: [DISTRO=<DISTRO>] [MACHINE=<MACHINE>] source <script> [BUILDDIR]\n")
    print("If no MACHINE is set, list all possible machines, and ask user to choose.")
    print("If no DISTRO is set, list all possible distros, and ask user to choose.")
    print("If no BUILDIR is set, it will be set to ''.")


# Check if the number of arguments is correct
def main():
    if len(sys.argv) > 2:
        usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
