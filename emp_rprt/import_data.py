import pandas as pd
from django.contrib.auth.models import User
from emp_rprt.models import Products, Progress, WorkflowStage, ProgressUpdated
import numpy as np

# Path to the CSV file in the project root directory
csv_file_path = './data2.csv'  # Replace with your CSV filename

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Replace NaN values with defaults (for example, Quantity with 0)
df.fillna({
    'SKU': 'Unknown SKU',         # Default SKU if missing
    'Description': 'No Titles',  # Default Description if missing
    'CP': 0,                      # Default Cost Price
    'SP': 0,                      # Default Selling Price
    'Color': 'N/A',     # Default Color
    'Quantity': 0,                # Default Quantity
    'Size': 'N/A',       # Default Size
}, inplace=True)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    # Check if the product already exists
    if not Products.objects.filter(sku=row['SKU']).exists():
        # Create the Product instance if it doesn't exist
        product = Products(
            sku=row['SKU'],                 # SKU from the CSV
            title=row['Description'],       # Description from the CSV
            cp=row['CP'],                   # Cost price from the CSV
            sp=row['SP'],                   # Selling price from the CSV
            details=row['Color'],           # Colors from the CSV
            quantity=int(row['Quantity']),  # Quantity from the CSV (converted to int)
            size=row['Size'],               # Size from the CSV
        )
        # Save the product
        product.save()

        # Get the initial workflow stage
        # workflow = WorkflowStage.objects.first()
        
        # # Create progress entries
        # Progress.objects.create(
        #     product=product,
        #     workflow_stage=workflow,
        #     status='completed',
        # )
        # Progress.objects.create(
        #     product=product,
        #     workflow_stage=workflow.next_stages.first(),
        #     status='not_started',
        # )

        workflow_first = WorkflowStage.objects.first()

        if workflow_first:
            Progress.objects.create(
                    product = product,
                    workflow_stage = workflow_first,
                    status = 'completed',
                )
            ProgressUpdated.objects.create(
                        product=product,
                        workflow_stage=workflow_first,
                        status_changed_to="completed",
                    )


            for stage in workflow_first.next_stages.all():
                    # print(progress.workflow_stage.next_stages)
                if stage:
                    Progress.objects.create(
                        product = product,
                        workflow_stage = stage,
                        status = 'not_started',
                    )
                    ProgressUpdated.objects.create(
                        product=product,
                        workflow_stage=stage,
                        status_changed_to="not_started",
                    )

print("CSV data has been loaded into the Django database.")
