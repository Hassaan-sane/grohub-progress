import pandas as pd
from emp_rprt.models import Products, Progress, WorkflowStage

# Path to the CSV file in the project root directory
csv_file_path = './data.csv'  # Replace with your CSV filename

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    # Create the Product instance
    if not Products.objects.filter(sku=row['SKU']).exists():

        product = Products(
            sku=row['SKU'],  # SKU from the CSV
            title=row['Description'],  # Description from the CSV
            cp=row['CP'],  # Cost price from the CSV
            sp=row['SP'],  # Selling price from the CSV
            details=row['Color'],  # Colors from the CSV
            quantity=row['Quantity'],  # Quantity from the CSV
            size=row['Size'],  # Size from the CSV # Slug from description
        )
        # Save the product
        product.save()
        workflow = WorkflowStage.objects.first()
        
        Progress.objects.create(
            product = product,
            workflow_stage = workflow,
            status = 'completed',
        )
        Progress.objects.create(
            product = product,
            workflow_stage = workflow.next_stages.first(),
            status = 'not_started',
        )

print("CSV data has been loaded into the Django database.")
