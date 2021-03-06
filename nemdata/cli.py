import click
import pandas as pd

from nemdata.databases import Files
from nemdata.use_cases import main as use_cases
from nemdata.mmsdm import reports as mmsdm_reports


@click.command()
@click.option(
    '--start', '-s', default='2018-01', help='start date (YYYY-MM)'
)
@click.option(
    '--end', '-e', default='2019-01', help='end date (incusive) (YYYY-MM)'
)
@click.option(
    '--reports', '-r', multiple=True, default=['nemde'], help='nemde, '+', '.join(mmsdm_reports.keys())
)
def main(start, end, reports):
    """nem-data is a tool to access NEM data"""
    click.echo('Hello from nem-data :)')
    click.echo(' ')

    end = str(pd.Timestamp(end) + pd.Timedelta('31D'))
    for report in reports:
        print(f'starting downloads for {report}')
        use_cases(report, start, end, Files(report))
