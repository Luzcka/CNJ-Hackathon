"""
Main script for data processing and final dataset generation

@date Oct 16, 2020
@author Inova Ixtepô
"""

from create_final_base import create_final_base, create_list_of_cnpj


def main():
    create_list_of_cnpj(number_cnpjs=250000, max_filiais=100)
    create_final_base()


if __name__ == '__main__':
    main()
