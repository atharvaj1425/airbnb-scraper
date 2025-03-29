// client/app/listing/[id]/page.js

import { notFound } from 'next/navigation';

export default async function ListingDetail({ params }) {
  const { id } = params;

  // For demo, fetch all listings and filter; ideally, use a dedicated endpoint.
  const res = await fetch('http://127.0.0.1:8000/api/listings/', { cache: 'no-store' });
  if (!res.ok) {
    throw new Error('Failed to fetch listings');
  }
  const listings = await res.json();
  const listing = listings.find((item) => String(item.id) === id);

  if (!listing) {
    notFound();
  }

  return (
    <div className="container mx-auto p-4">
      {listing.image_urls && listing.image_urls.length > 0 && (
        <img
          src={listing.image_urls[0]}
          alt={listing.title}
          className="w-full h-64 object-cover rounded mb-4"
        />
      )}
      <h1 className="text-3xl font-bold mb-2">{listing.title}</h1>
      <p className="text-gray-600 mb-2">{listing.location}</p>
      <p className="text-lg font-bold mb-2">${listing.price_per_night} per night</p>
      <p className="text-sm text-gray-500 mb-2">
        {listing.ratings} ★ ({listing.reviews} reviews)
      </p>
      <p className="mb-4">{listing.description}</p>

      <div>
        <h2 className="text-xl font-semibold mb-2">Amenities</h2>
        <ul className="list-disc ml-6">
          {listing.amenities && listing.amenities.map((amenity, index) => (
            <li key={index}>{amenity}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h2 className="text-xl font-semibold mb-2">Host Information</h2>
        <p className="text-lg">{listing.host && listing.host.name}</p>
      </div>
    </div>
  );
}
