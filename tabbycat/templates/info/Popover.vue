<template>

  <div class="hover-target"
       @mouseenter="showPopover" @mouseleave="hidePopover">

    <slot>
      {{ content }}
    </slot>

    <ul class="list-group list-group-item-flush" hidden ref="popHTML">

      <li v-for="item in popContent" class="list-group-item">
        <a v-if="item['link']" :href="item['link']">
          <span v-html="item['text']"></span>
        </a>
        <span v-else>
          <span v-html="item['text']"></span>
        </span>
      </li>

    </ul>
  </div>

</template>

<script>
// Inheriting componets should provide a getPopOverTitle() method
// Along with providing an element with the "popover-raw" class as a direct
// descendent of the component's root template
// They can then trigger showPopover; ie "@mouseover="showPopover""
// Note that once triggered, it will handle its own show/hide events

export default {
  props: {
    cellData: Object,
  },
  computed: {
    popContent: function() {
      return this.cellData['content']
    },
  },
  methods: {
    showPopover: function(event) {

      // Grab popover content from actual render html
      if (this.popContent.length > 0) {
        var content = this.$refs.popHTML.innerHTML
      } else {
        var content = ""
      }

      // Popovers are disabled sometimes; e.g. on a scrolling draw page
      if ($(event.target).hasClass("disable-hover") === false){

        // Unclear if waiting for nextTick helps here, but there were errors
        // being thrown where the tooltip element's this.config.template was
        // null; possibly because the DOM hadn't been resolved yet?
        this.$nextTick(function() {

          $(event.target).popover({
            animation: true,
            trigger: 'manual',
            placement: 'left',
            html: true,
            title: this.cellData['title'],
            content: content,
            container: event.target, // Must be same as what triggers the event
            offset: '0,-40' // Shift so hover is easier
          })
          $(event.target).popover('show')

        })
      }
    },
    hidePopover: function(event) {
      $(event.target).popover('dispose');
    },
  }
}
</script>
