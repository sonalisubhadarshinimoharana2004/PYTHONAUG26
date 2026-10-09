function Product({ product_title, description, price }) {
  return (
    <div>
      <h2>{product_title}</h2>
      <p>{description}</p>
      <h3>Price: ₹{price}</h3>
    </div>
  );
}

export default Product;