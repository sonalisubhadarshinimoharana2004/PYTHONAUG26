import React from "react";
import { useParams, useSearchParams } from "react-router";

function User() {
  const { id } = useParams();

  const [searchParams] = useSearchParams();

  return (
    <div>
      <h1>User Details</h1>

      <h2>Path Parameter</h2>
      <p>User ID: {id}</p>

      <h2>Query Parameters</h2>
      <p>Name: {searchParams.get("name")}</p>
      <p>Age: {searchParams.get("age")}</p>
      <p>City: {searchParams.get("city")}</p>

      <h2>All Query Values</h2>

      {Array.from(searchParams.entries()).map(([key, value]) => (
        <p key={key}>
          {key}: {value}
        </p>
      ))}
    </div>
  );
}

export default User;
