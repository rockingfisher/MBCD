<template>
  <div class="border text-start">
    <div class="row">
      <th class="col-4 d-inline">게시글 번호: {{ review.id }}</th>
      <router-link
        :to="{ name: 'ReviewDetailView', params: { review_id: review.id } }"
        class="col-4 d-inline"
      >
        <th>게시글 제목: {{ review.title }}</th>
      </router-link>
      <th class="col-4 d-inline">작성자: {{ review.username }}</th>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewItem",
  props: {
    review: Object,
  },
};
</script>

<style scoped></style>
