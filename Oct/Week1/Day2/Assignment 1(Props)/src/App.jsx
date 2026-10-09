import Product from "./Product";

function App() {
  return (
    <div>
      <h1>Product Details</h1>

      <Product
        product_title="Laptop"
        description="This is a powerful laptop for students and developers."
        price="80000"
      />
    </div>
  );
}

export default App;