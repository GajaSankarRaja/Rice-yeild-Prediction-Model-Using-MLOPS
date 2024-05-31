from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserInput
from .serializer import UserInputSerializer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class UserInputViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            input1 = serializer.validated_data.get('input1')
            input2 = serializer.validated_data.get('input2')

            # Load the dataset
            d = pd.read_csv('C:\\Users\\gajas\\Datasets\\dataorg.csv')
            d = d[['RICE PRODUCTION (1000 tons)', 'RICE YIELD (Kg per ha)', 'RICE AREA (1000 ha)']]

            # Split features and target
            x = d[['RICE PRODUCTION (1000 tons)', 'RICE AREA (1000 ha)']]
            y = d['RICE YIELD (Kg per ha)']

            # Train-test split
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

            # Fit the regression model
            rg = LinearRegression()
            rg.fit(x_train, y_train)

            # Predict the output based on user input
            # Predict the output based on user input
            user_input = [[float(input1), float(input2)]]
            prediction = rg.predict(user_input)


            # Return the prediction to the frontend
            return Response({'prediction': prediction[0]}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
